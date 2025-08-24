
from django.urls import path
from . import views

urlpatterns = [
     path('',views.task_list, name='task_list'),
     path('tasks/add',views.add_task, name='add_task'),
     path('reports/',views.completed_task_list, name='completed_task_list'),
     path("tasks/<int:task_id>/update-status/", views.update_status, name="update_status"),
     path("tasks/<int:task_id>/edit_task/", views.edit_task, name="edit_task"),
     path("tasks/<int:task_id>/delete/", views.delete_task, name="delete_task"),
 ]
 