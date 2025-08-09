<<<<<<< HEAD
from django.urls import path
from task_app import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),
    path('update/<int:pk>', views.TaskUpdateView.as_view(), name='task_update')
=======
from django.urls import path
from task_app import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),
    path('update/<int:pk>', views.TaskUpdateView.as_view(), name='task_update')
>>>>>>> d379b6e30c07f99ec4aad97fa6be016ca6a18f5e
]