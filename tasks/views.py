from django.shortcuts import redirect, render

from tasks.forms import TaskForm
from tasks.models import Task


# Create your views here.
def task_list(request):
    dos = Task.objects.all().order_by('-deadline')
    return render(request,'tasks/task_list.html',{'tasks':dos})
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm()
    return render(request, "tasks/task_list.html")

