from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)

class Task(models.Model):
    TASK_PENDING='P'
    TASK_COMPLETE='C'
    
    COMPLETION_CHOICES =[
        (TASK_PENDING,'Pending'),
        (TASK_COMPLETE,'Complete')
    ]
    
    NOT_URGENT='N'
    URGENT='Y'
    
    URGENCY_CHOICES=[
        (NOT_URGENT,'Not urgent'),
        (URGENT,'Urgent')
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    completion_status = models.CharField(max_length=255,choices=COMPLETION_CHOICES,default=TASK_PENDING)
    is_it_urgent = models.CharField(max_length=255,choices=URGENCY_CHOICES,default=NOT_URGENT)
    due_by_date = models.DateField(null=True)
    task_creation_date = models.DateField(auto_now_add=True)
    
