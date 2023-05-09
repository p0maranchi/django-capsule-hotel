from django.urls import path
from . import views


urlpatterns = [
    path('', views.capsule_list, name = 'capsule_list'),
    path('<slug:slug>/', views.capsule_detail, name = 'capsule_detail'),

]