
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from users.views import * #for register
from django.contrib.auth import views as auth_views #for login/logout

urlpatterns = [
    path('admin/', admin.site.urls),



    path('register/',register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
]
