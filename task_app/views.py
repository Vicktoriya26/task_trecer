from django.shortcuts import render
from django.views.generic import ListView, UpdateView

from task_app.models import Task

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task_form.html'
    

