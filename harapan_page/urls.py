from django.urls import path
from .views import harapan_page, show_harapan, show_harapan_json, delete_harapan

app_name = 'harapan_page'

urlpatterns = [
    path('', show_harapan, name='show_harapan'),
    path('add-harapan/', harapan_page, name='harapan_page'),
    path('show-json/', show_harapan_json, name='show-json'),
    path('delete-harapan/<int:key>/', delete_harapan, name='delete'),
]