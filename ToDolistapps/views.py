from django.shortcuts import render
from django.http import JsonResponse
from .models import Task
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Taskserializers

# Create your views here.

@api_view(['GET'])      
def ApiOverView(request):
    return Response("this api base point" ,safe= False)

@api_view(['GET'])  
def TaskList(request):
    task = Task.objects.all().order_by("-id")
    serializer = Taskserializers(task,many=True)
    return Response(serializer.data)

from rest_framework import status
@api_view(['GET'])  
def TaskDetialView(request , pk):
    task = Task.objects.get(id=pk)
    serializer = Taskserializers(task,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def TaskCreateView(request):
    serializer = Taskserializers(data =request.data)
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

@api_view(['POST'])
def TaskUpdateview(request, pk):
    task = Task.objects.get(id=pk)
    serializer = Taskserializers( instance=task  ,data =request.data)
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

@api_view(['DELETE'])
def TaskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response('Item sucessfully deleted')


    