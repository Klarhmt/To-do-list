from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from . import models,serializers


# Create your views here.

class TaskViewSet(ModelViewSet):
    queryset = models.Task.objects.all()
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.request.method=='POST':
            return serializers.CreateTaskSerializer
        return serializers.TaskSerializer