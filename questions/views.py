from django.shortcuts import render
from .models import FAQ, Post, Comment

# Create your views here.
def show_questions(request):
    questions = FAQ.objects.all()
    posts = Post.objects.all()
    
    context = {
        'questions' : questions,
        'posts' : posts,
    }
    
    return render(request, 'questions.html', context)