from django.shortcuts import render

# Create your views here.

def example_app(request):
    return render(request, 'example-app.html')