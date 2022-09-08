from django.urls import path
from . import views


urlpatterns=[
    path('', views.welcomepage),
    path('registration/',views.home_page),
]