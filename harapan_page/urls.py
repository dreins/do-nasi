from django.urls import path
from .views import harapan_page

app_name = 'harapan_page'

urlpatterns = [
    path('', harapan_page, name='harapan_page'),
]