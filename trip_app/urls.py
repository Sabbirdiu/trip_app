from django.urls import path
from . import views
from .views import PostListView,PostCreateView

urlpatterns = [
  
   path('dashboard/',views.dashboard,name='dashboard'),
   path('travels/',PostListView.as_view(),name='travel'),
   path('new_post/',PostCreateView.as_view(),name ='post-create'),
 
]