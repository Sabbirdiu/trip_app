from django.urls import path
from . import views
from .views import PostCreateView,PostDetailView

urlpatterns = [
  
   path('dashboard/',views.dashboard,name='dashboard'),
#    path('travels/',PostListView.as_view(),name='travel'),
   path('post/',PostCreateView.as_view(),name ='post-create'),
   path('travel/',views.todos_for_user,name='travel'),
    # path('travel/<id>/', views.detail_view ), 
    path('travel/<int:pk>/',PostDetailView.as_view(),name ='post-detail'),

 
]