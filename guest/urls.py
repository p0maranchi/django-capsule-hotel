from django.urls import path
from .views import UserPasswordChangeView
from . import views

urlpatterns = [
    path('login_user/', views.login_user, name='login'),
    path('logout_user/', views.logout_user, name='logout'),
    path('register_user/', views.register_user, name='register'),
    path('password-change/', UserPasswordChangeView.as_view(), name='password_change'), 
]
