from django.shortcuts import render
from django.views import View
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from . import models,serializers


# Create your views here.

def task_list_view(request):
    urgent_tasks = models.Task.objects.filter(is_it_urgent='Y')
    pending_tasks = models.Task.objects.filter(completion_status='P')
    completed_tasks = models.Task.objects.filter(completion_status='C')
    
    context = {
        'urgent_tasks':urgent_tasks,
        'pending_tasks':pending_tasks,
        'completed_tasks':completed_tasks
    }
    return render(request,'task_list_page.html',context)