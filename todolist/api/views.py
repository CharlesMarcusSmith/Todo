from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer

from .models import Task

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    # urls we are going to create
    #By returning this, it allows anyone working on our API to view our url patterns.
    api_urls = {
        'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
    }

    return Response(api_urls)

#GET ALL
@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()                       #Querying the Task object, saved as variable
    serializer = TaskSerializer(tasks, many=True)    # Set serializer, passing in the tasks variable, and returning many responses
    return Response(serializer.data)




#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV

#SEARCH
@api_view(['GET'])
def taskDetail(request, pk):
    task = Task.objects.get(id=pk)                        
    serializer = TaskSerializer(task, many=False)    
    return Response(serializer.data)




#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



#CREATE
@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()    
    return Response(serializer.data)

#UPDATE
@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task ,data=request.data)

    if serializer.is_valid():
        serializer.save()    
    return Response(serializer.data)