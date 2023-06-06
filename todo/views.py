from django.shortcuts import get_object_or_404, redirect, render
from .models import Task

def addTask(req):
    task = req.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

def markAsDone(req, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def undoTask(req, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def editTask(req, pk):
    task = get_object_or_404(Task, pk=pk)
    if req.method == 'POST':
        new_task = req.POST['task']
        task.task = new_task
        task.save()
        return redirect('home')
    else:
        ctx = {
            'task': task,
        }
        return render(req, 'edit_task.html', ctx)
    
def deleteTask(req, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')
