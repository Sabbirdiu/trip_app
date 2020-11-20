from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,CreateView
from django.contrib.auth.models import User
from .models import Trip
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
@login_required 
def dashboard(request):
    return render(request,'dashboard.html')
class PostListView(LoginRequiredMixin,ListView):
    model = Trip
    template_name = 'travels.html'
    context_object_name = 'travels'    
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Trip
    fields=['destination','description','plan','travel_start_date','travel_end_date']   
    template_name='new_post.html'

    def form_valid(self,form):#without a author other user cannot create a post
        form.instance.author = self.request.user
        return super().form_valid(form)    