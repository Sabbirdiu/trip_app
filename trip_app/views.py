from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,CreateView,DetailView
from django.contrib.auth.models import User
from .models import Trip
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
@login_required 
def dashboard(request):
    return render(request,'dashboard.html')    
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Trip
    fields=['destination','description','plan','travel_start_date','travel_end_date']   
    template_name='new_post.html'

    def form_valid(self,form):#without a author other user cannot create a post
        form.instance.author = self.request.user
        return super().form_valid(form)    
@login_required
def todos_for_user(request):
    todos = Trip.objects.filter(author=request.user)
    travels = Trip.objects.all()
    context = {
          'todos' : todos,
          'travels' : travels

    }
    return render(request, 'travel.html', context)          
class PostDetailView(DetailView):
    model = Trip  
    template_name = 'detail_view.html'