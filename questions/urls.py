from django.urls import path
from questions.views import *

app_name = 'questions'

urlpatterns = [
    path('', show_questions, name='show_questions'),
]