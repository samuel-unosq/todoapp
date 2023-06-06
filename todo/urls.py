from django.urls import path
from . import views

urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
    path('mark_as_done/<int:pk>/', views.markAsDone, name='mark_as_done'),
    path('undo_task/<int:pk>/', views.undoTask, name='undo_task'),
    path('edit_task/<int:pk>/', views.editTask, name='edit_task'),
    path('delete_task/<int:pk>/', views.deleteTask, name='delete_task'),
]
