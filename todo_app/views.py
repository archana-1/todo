from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from todo_app.models import Task


# Create your views here.
def addtask(request):

    task = request.POST['addtask_in']
    Task.objects.create(task = task)
    return redirect('home')

def markasdone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def edittask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        # take the data from the form
        task.task = request.POST['update_t']
        task.save()
        return redirect('home')
    else:
        return render(request, 'edittask.html', {'task' : task})
    
def deletetask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')