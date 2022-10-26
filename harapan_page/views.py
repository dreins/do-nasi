import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from harapan_page.models import HarapanDonatur
from django.contrib import messages
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse

# Create your views here.
# @login_required(login_url='/todolist/login/')

@csrf_exempt
def show_harapan(request):
    data_harapan = HarapanDonatur.objects.all()
    context = {
        # 'username': request.COOKIES['username'],
        # 'last_login': request.COOKIES['last_login'],
        'mytodo': data_harapan,
    }
    return render(request, "harapan_page.html", context)

@csrf_exempt
def harapan_page(request):
    if request.method == 'POST':
        user = request.user
        text = request.POST.get('text')
        harapan_image = request.POST.get('harapan_image')
        harapan = HarapanDonatur.objects.create(
            user=user, text=text, harapan_image=harapan_image)
        if harapan == None:
            messages.info(request, 'Silahkan masukkan harapan anda!')
        else:
            return JsonResponse({'message' : 'Harapan Created!', 'error': False})

    return JsonResponse({'message' : 'Harapan Uploaded!'})

@csrf_exempt
def show_harapan_json(request):
    data = HarapanDonatur.objects.filter(user=request.user).order_by('-likes')

    return HttpResponse(
        serializers.serialize("json", data), 
        content_type="application/json"
    )