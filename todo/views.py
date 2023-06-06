from django.shortcuts import redirect
from .models import Task

def addTask(req):
    task = req.POST['task']
    Task.objects.create(task=task)
    return redirect('home')
