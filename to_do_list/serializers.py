from rest_framework.serializers import ModelSerializer
from . import models

class TaskSerializer(ModelSerializer):
    class Meta:
        model = models.Task
        fields = ['id','title','description','completion_status','is_it_urgent','due_by_date','creation_date']
        
class CreateTaskSerializer(ModelSerializer):
    class Meta:
        model = models.Task
        fields = ['id','title','description','is_it_urgent','due_by_date']