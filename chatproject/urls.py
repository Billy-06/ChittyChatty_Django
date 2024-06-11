from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
import chatapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', chatapp.views.home, name='home'),  
    path('chat/', include('chatapp.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='chatapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='chatapp/logout.html'), name='logout'),
]
