from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.TodoListAPIView.as_view(), name='todo-list'),
    path('todos/<int:pk>/', views.TodoDetailAPIView.as_view(), name='todo-detail'),
]