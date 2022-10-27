from django.urls import path
from .views import harapan_page, show_harapan

app_name = 'harapan_page'

urlpatterns = [
    path('', show_harapan, name='show_harapan'),
    path('add-harapan/', harapan_page, name='harapan_page'),
]