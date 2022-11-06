from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.urls import path

from . import views

urlpatterns = [
    path(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]
