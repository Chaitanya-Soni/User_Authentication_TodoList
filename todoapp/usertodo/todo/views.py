from django.shortcuts import render
from . models import todo
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView, UpdateView ,DeleteView

from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'todo/login.html'
    fields= '__all__'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('tasks')

class TaskList( ListView):
    model = todo
    context_object_name = 'tasks'
class TaskDetail( DetailView):
    model = todo
    context_object_name = 'task'
    template_name = 'todo/task.html'
class TaskCreate(CreateView):
    model = todo
    fields = '__all__'
    success_url = reverse_lazy('tasks')
class TaskUpdate(UpdateView):
    model = todo
    fields = '__all__'
    success_url = reverse_lazy('tasks')
class TaskDelete(DeleteView):
    model = todo
    context_object_name = 'task'
    success_url = reverse_lazy('tasks') 