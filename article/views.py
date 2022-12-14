from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import HttpResponse, render
from django.core import serializers
from article.forms import article_form, comment_form
import datetime
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json


from article.models import Article, Comment
def article(request):
    article_item = Article.objects.all()
    username = request.user
    context={
        'article_item':article_item,
        'form' :article_form,
        'user': username
    }
    return render(request,'article.html',context)


def get_article_json(request):

    data = []
    article = Article.objects.all()
    
    for item in article:
        data.append({
            "pk" : item.pk,
            "fields" : {
                "user" : { 
                        "username" : item.user.username,
                        "name"     : item.user.name,
                        "role"     : item.user.role
                        },
               
                "date" : item.date,
                "title" : item.title,
                "body" : item.body,
                "slug":item.slug,
                
            }
        })
    return JsonResponse(data, safe=False)

def get_comments_json(request):
    comments = Comment.objects.all()
    return HttpResponse(serializers.serialize('json', comments))


def add_article(request):
    posts = Article.objects.all()
    response_data = {}
    if request.method == "POST":
        username = request.user
        date_user = datetime.date.today()
        title_user = request.POST.get('title')
        body_user = request.POST.get('body')
        slug_user = request.POST.get('slug')

        new_article = Article(user=username, date=date_user, title=title_user,body=body_user,slug=slug_user)
        new_article.save()
        return JsonResponse({
            "pk" : new_article.pk,
            "fields" : {
                "user" : { 
                        "username" : new_article.user.username,
                        "name"     : new_article.user.name,
                        "role"     : new_article.user.role
                        },
               
                "date" : new_article.date,
                "title" : new_article.title,
                "body" : new_article.body,
                "slug":new_article.slug,
                
            }
        })

    return render(request, 'article.html', {'posts':posts})

@login_required(login_url='../login/')
def detail(request,slug):
    # posts = Article.objects.get(slug=slug)
    
    posts = Article.objects.get(slug=slug)


    if request.method == "POST":
        form = comment_form(request.POST)

        if form.is_valid():
            name_user = request.user
            post_user = posts
            date_user = datetime.date.today()
            comment_user = request.POST.get('body')
            new_article = Comment(post=post_user, name= name_user, body=comment_user, date_added = date_user)
            new_article.save()
           

            return redirect('article:detail',slug=posts.slug)
    context={
        'posts':posts,
        'form' :comment_form,
    }
    return render(request,'detail_article.html',context)


   
