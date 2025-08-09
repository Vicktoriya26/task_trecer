from django.urls import path
from task_app import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),
    path('update/<int:pk>', views.TaskUpdateView.as_view(), name='task_update')
]