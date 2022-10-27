from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from page_overview.forms import create_form
from landing_page.models import Pengguna
from django.http import JsonResponse
from django.core import serializers
from page_overview.models import Donasi
# Create your views here.

# @login_required(login_url='/landing_page/login/')
def show_overview(request):
    # if request.user.is_authenticated:
        # data = Pengguna.objects.filter(user = request.user)
        # last_login_info = request.COOKIES.get('last_login', 'not found')
        # if (last_login_info == 'not found'):
        #     return redirect('landing_page:login')
        role = request.user.role
        context = {
            # 'roles': True if role == "Donatur" else False,
            # 'list': data,
            # 'user_name': request.user.username,
            # 'last_login': request.COOKIES.get('last_login', 'not found'),
        }
        return render(request, "page_overview.html", context)
    # else:
    #    return redirect('landing_page:login') 

# @login_required(login_url='/landing_page/login/')
def add_donasi_ajax(request):
    # if request.user.is_authenticated:
        form = create_form(request.POST)
        data = {}   
        if request.method == 'POST' and form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            new_task = Donasi.objects.create(title=title, description=description)
            data['title'] = title
            data['description'] = description
    #         data['user'] = request.user
    #         return JsonResponse(data)
    # else:
    #     return redirect('landing_page:login')

def get_json(request):
    data = Donasi.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def do_donation(request, id):
    if request.user.is_authenticated:
        task = Donasi.objects.get(id=id)
        task.save()
        return JsonResponse({'msg':'success'})
    else:
        return redirect('landing_page:login')