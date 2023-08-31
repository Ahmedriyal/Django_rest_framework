from django.urls import path

from django_rest_api.views import index, person

urlpatterns = [
    path('index/', index),
    path('person/', person),
]