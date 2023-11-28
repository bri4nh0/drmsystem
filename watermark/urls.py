from django.contrib import admin
from django.urls import path
from drmsystem.watermark import views



urlpatterns = [
    path('/', views.home, name='index')
]