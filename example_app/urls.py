from django.urls import path
from example_app.views import example_app

app_name = 'example_app'

urlpatterns = [
    path('', example_app, name='example_app'),
]