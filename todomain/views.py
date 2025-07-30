

from django.shortcuts import render

from todo_app.models import Task


def home(request):
    tasks = Task.objects.filter(is_completed = False).order_by('-updated_at')
    return render(request, 'home.html', {'tasks': tasks})