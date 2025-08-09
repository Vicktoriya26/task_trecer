from winreg import DeleteKey
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from task_app.forms import TaskForm
from task_app.models import Task

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = Task.objects.filter(author=self.request.user)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['welcome_message'] = 'Ласкаво просимо!'
        
        return context

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'due_date']
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'task_form.html'
    form_class = TaskForm
    success_url = reverse_lazy('task_list')


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task_form.html'
    form_class = TaskForm
    success_url = reverse_lazy('task_list')
    

