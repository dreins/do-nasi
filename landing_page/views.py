from django.shortcuts import render


# Landing page
def landing_page(request):
    return render(request, 'landing-page.html')