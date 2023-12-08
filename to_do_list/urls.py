from django.urls import include,path
from rest_framework_nested import routers
from . import views


urlpatterns =[
    path('tasks/',views.task_list_view,name='task_list_view')
]