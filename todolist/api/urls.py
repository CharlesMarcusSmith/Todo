from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('task-list/', views.taskList, name="task-list"), 
    path('task-detail/<str:pk>', views.taskList, name="task-detail"), #passing in pk for search
    path('task-create/', views.taskCreate, name="task-create"), 
]
    