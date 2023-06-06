
from django.shortcuts import render
from todo.models import Task


def home(req):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    # completed_tasks = Task.objects.filter(is_completed=True)
    ctx = {
        'tasks': tasks,
    }

    return render(req, 'home.html', ctx)
