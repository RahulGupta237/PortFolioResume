from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('exp/',views.experience,name='services'),
]
