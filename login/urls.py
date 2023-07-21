from django.contrib import admin
from login import views
from django.urls import path

urlpatterns = [
    path('login/', views.index, name='login'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]
