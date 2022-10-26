from django.urls import path
from page_overview.views import *

app_name = 'page_overview'

urlpatterns = [
    path('', show_overview, name='show_overview'),
    path('add/', add_task_ajax, name = 'add_task_ajax')
]
    
    