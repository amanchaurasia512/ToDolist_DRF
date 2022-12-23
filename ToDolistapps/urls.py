from django.contrib import admin
from django.urls import path
from .import views 

urlpatterns = [
    path('', views.ApiOverView),
    path('task_list/', views.TaskList, name= 'task_list'),
    path('task_detial/<str:pk>/', views.TaskDetialView, name='task_detial'),
    path('task_create/', views.TaskCreateView, name= 'task_create'),
    path('task_update/<str:pk>/', views.TaskUpdateview, name='task_update'),
    path('task_delete/<str:pk>/', views.TaskDelete, name='task_delete'),
]
