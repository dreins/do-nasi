import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.core import serializers
from landing_page.models import Pengguna
from page_overview.models import Donasi
from .forms import FormLogin, FormRegister, FormLogin
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import AnonymousUser
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required


# Landing page
def landing_page(request):
	return render(request, "landing-page.html")

	

# Register
# def register(request):
#     context = {}
#     if request.method == "POST":
#         form = FormRegister(request.POST)
#         data = {}
#         if form.is_valid():
#             form.save()
#             data['success'] = True
#             return HttpResponse(json.dumps(data), content_type='application/json')
#         else: 
#             data['error'] = form.errors
#             data['form'] = form
#             data['success'] = False
#             return HttpResponse(json.dumps(data), content_type='application/json')

#     form = FormRegister()
#     context = {'form':form}
#     return render(request, 'register.html', context)

@csrf_exempt
def register(request):
	context = {}
	if request.POST:
		form = FormRegister(request.POST)
		data = {}
		if form.is_valid():
			form.save()
			data['success'] = True
			return HttpResponse(json.dumps(data), content_type='application/json')
		else:
			data['error'] = form.errors
			data['success'] = False
			context['registration_form'] = form
			return HttpResponse(json.dumps(data), content_type='application/json')

	else:
		form = FormRegister()
		context['registration_form'] = form
	return render(request, 'register.html', context)

@csrf_protect
def login_page(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('landing_page:landing_page')

    if request.POST:
        form = FormLogin(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('landing_page:landing_page')
				
    else:
        form = FormLogin()
    context['login_form'] = form
	
    return render(request, "login.html", context)

def logout_view(request):
	logout(request)
	request.session.flush()
	request.user = AnonymousUser
	return redirect("landing_page:landing_page")

def get_json_penyalur(request):
	if request.user.is_authenticated:
		if request.user.role == "Penyalur":
			pengguna = Pengguna.objects.get(username = request.user.username)
			list = Donasi.objects.filter(user = pengguna)
			return HttpResponse(serializers.serialize("json", list), content_type="application/json")
		else :
			list = Donasi.objects.all()
			return HttpResponse(serializers.serialize("json", list), content_type="application/json")
	else:
		return HttpResponse(status=204)
