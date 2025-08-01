
from django.urls import path, include
from . import views

urlpatterns =[
    path('addtask/', views.addtask, name='addtask'),
    path('markasdone/<int:pk>/', views.markasdone, name='markasdone'),
    # edit feature
    path('edittask/<int:pk>/', views.edittask, name='edittask'),
    # delete task
    path('deletetask/<int:pk>/', views.deletetask, name='deletetask'),
]