from django.urls import path
from questions.views import *

app_name = 'questions'

urlpatterns = [
    path('', show_questions, name='show_questions'),
    path('json/all-posts/', get_posts_json, name="get_posts"),
    path('json/all-comments/<int:id>', get_comments_json, name="get_comments"),
    path('add-post/', add_post, name='add_post'),
    path('add-comment/<int:id>', add_comment, name='add_comment'),
    path('delete-post/<int:id>', delete_post, name='delete_post'),
    path('delete-comment/<int:id>', delete_comment, name='delete_comment')
]