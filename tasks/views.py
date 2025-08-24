import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from tasks.forms import TaskForm
from tasks.models import Task


# Create your views here.
def task_list(request):
    dos = Task.objects.filter(status='I').order_by('-deadline')
    return render(request,'tasks/task_list.html',{'tasks':dos})
def add_task(request):
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm()
      
    return render(request, "tasks/task_list.html")

def update_status(request,task_id):
    task = get_object_or_404(Task,id = task_id)
    if request.method == "POST":
        data = json.loads(request.body)  # parse JSON body
        status = data.get('status')
        task.status = status
        task.save()
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Invalid request'}, status=400)
        
def completed_task_list(request):
    dones = Task.objects.filter(status = 'C')
    return render(request,'tasks/Reports.html',{'tasks':dones})
def edit_task(request,task_id):
    task = get_object_or_404(Task, id= task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task_list")
        else:
            return render(request, "tasks/task_list.html", {
                "tasks": task,
                "form": form,  # keep errors + user input
                "edit_task_id": task.id,  # tell template which modal to open again
            })

def delete_task(request,task_id):
    task = get_object_or_404(Task,id = task_id)
    if request.method == "POST":
        task.delete()
        return JsonResponse({'success': True}) 
    return JsonResponse({'error': 'Invalid request'}, status=400)


