from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    # path('suggest_place/', views.suggest , name ='suggest'),
    # path("details/", views.details, name="more_details"),
    path("landing_page/", views.landing , name ='landing'),
]
