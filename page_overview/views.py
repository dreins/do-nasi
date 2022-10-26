from audioop import add
from hashlib import new
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from page_overview.forms import create_form
from landing_page.models import Pengguna
from django.http import JsonResponse
# Create your views here.

# @login_required(login_url='/landing_page/login/')
def show_todolist(request):
    # if request.user.is_authenticated:
        data = Pengguna.objects.filter(user = request.user)
        last_login_info = request.COOKIES.get('last_login', 'not found')
        if (last_login_info == 'not found'):
            return redirect('landing_page:login')
        context = {
            'list': data,
            'user_name': request.user.username,
            'last_login': request.COOKIES.get('last_login', 'not found'),
        }
        return render(request, "page_overview.html", context)

    # else:
    #    return redirect('landing_page:login') 

# @login_required(login_url='/landing_page/login/')
def add_task_ajax(request):
    # if request.user.is_authenticated:
        form = create_form(request.POST)
        data = {}   
       
        if request.method == 'POST' and form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            new_task = Pengguna.objects.create(title=title, description=description, user=request.user)
            data['title'] = title
            data['description'] = description
            data['user'] = request.user
            return JsonResponse(data)
    # else:
    #     return redirect('landing_page:login')