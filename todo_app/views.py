from django.http import HttpResponse
from django.shortcuts import render, redirect
from todo_app.models import Task


# Create your views here.
def addtask(request):

    task = request.POST['addtask_in']
    Task.objects.create(task = task)
    return redirect('home')