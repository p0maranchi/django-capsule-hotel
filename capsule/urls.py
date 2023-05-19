from django.urls import path
from . import views


urlpatterns = [
    path('', views.capsuleList, name = 'capsuleList'),
    path('<slug:slug>/', views.capsuleDetail, name = 'capsuleDetail'),

]