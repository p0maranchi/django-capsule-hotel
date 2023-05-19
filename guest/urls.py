from django.urls import path
from .views import UserPasswordChange
from . import views

urlpatterns = [
    path('login_user/', views.loginUser, name='login'),
    path('logout_user/', views.logoutUser, name='logout'),
    path('register_user/', views.registerUser, name='register'),
    path('password-change/', UserPasswordChange.as_view(), name='passwordChange'), 
]
