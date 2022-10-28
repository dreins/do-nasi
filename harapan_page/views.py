from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from harapan_page.models import HarapanDonatur
from landing_page.models import Pengguna
from django.contrib import messages
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse


# @login_required(login_url='/login/')
#@csrf_exempt
#def show_harapan(request):
#   if request.user.is_authenticated:
#        role = request.user.role
#        if role == "Penyalur":
#            pengguna = Pengguna.objects.get(username=request.user.username)
#            data_harapan = HarapanDonatur.objects.filter(user=pengguna)
#            context = {
#                'roles': True,
#               'data_harapan': data_harapan,
#            }
#            return render(request, "harapan_page.html", context)
#        else:
#            data_harapan = HarapanDonatur.objects.all()
#            context = {
#                'roles': False,
#                'data_harapan': data_harapan,
#            }
#            return render(request, "harapan_page.html", context)
#    else:
#        return redirect('landing_page:login')

def show_harapan(request):
    if request.user.is_authenticated:
        data_harapan = HarapanDonatur.objects.all()
        context = {
            'data_harapan': data_harapan,
        }
        return render(request, "harapan_page.html", context)
    else:
        return redirect('landing_page:login')


@login_required(login_url='/login/')
@csrf_exempt
def harapan_page(request):
    if request.method == 'POST':
        user = request.user
        text = request.POST.get('text')
        HarapanDonatur.objects.create(
           user=user, text=text, username=user, email = user.get_email())
        # HarapanDonatur.objects.all().delete()
        return JsonResponse({'message': 'Harapan Created!', 'error': False})


@csrf_exempt
def show_harapan_json(request):
    data = HarapanDonatur.objects.all()

    return HttpResponse(
        serializers.serialize("json", data),
        content_type="application/json"
    )

@login_required(login_url='/login/')
@csrf_exempt
def delete_ajax(request, key):
    if request.method == 'POST':
        mytask = get_object_or_404(HarapanDonatur, user = request.user, pk = key)
        mytask.delete()
        
    return JsonResponse({'error': False})
