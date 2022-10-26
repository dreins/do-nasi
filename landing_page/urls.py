from django.urls import path
from .views import landing_page

app_name = 'landing_page'

urlpatterns = [
    path('', landing_page, name='landing_page'),
#     path('register/', register_penyalur, name='register-penyalur'), 

]