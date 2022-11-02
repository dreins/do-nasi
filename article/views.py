
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
    article = Article.objects.all()
    return HttpResponse(serializers.serialize('json', article))

def get_comments_json(request):
    article = Article.objects.all()
    comments = Comment.objects.all()
    return HttpResponse(serializers.serialize('json', comments))

# def add_article(request):
#     if request.method == "POST":
#         data = json.loads(request.POST['data'])

#         new = Article(user=data["user"], date=data["date"], title=data["title"], body=data["body"], slug=data["slug"])
#         new.save()

#         return HttpResponse(serializers.serialize("json", [new]), content_type="application/json")

#     return HttpResponse()

def add_article(request):
    posts = Article.objects.all()
    response_data = {}
    if request.method == "POST":
        username = request.user
        date_user = datetime.date.today()
        title_user = request.POST.get('title')
        body_user = request.POST.get('body')
        slug_user = request.POST.get('slug')

        response_data['user'] = username
        response_data['date'] = date_user
        response_data['title'] = title_user
        response_data['body'] = body_user
        response_data['slug'] = slug_user

        Article.objects.create(
            user = username,
            date = date_user,
            title = title_user,
            body = body_user,
            slug = slug_user
        )

        return JsonResponse(response_data)

    return render(request, 'article.html', {'posts':posts})

@login_required(login_url='../login/')
def detail(request,slug):
    # posts = Article.objects.get(slug=slug)
    try:
        posts = Article.objects.get(slug=slug)
    except Comment.DoesNotExist:
        posts = None

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


   
