from django.urls import path
from page_overview.views import *

app_name = 'page_overview'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('add/', add_task_ajax, name = 'add_task_ajax')
]
    
    