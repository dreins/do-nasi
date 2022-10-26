from django.shortcuts import render

# Create your views here.
def harapan_page(request):
    return render(request, 'harapan_page.html')