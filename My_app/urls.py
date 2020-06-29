from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

    path('', views.index, name='home'),
    path('contacts', views.contacts, name='contacts'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('galery', views.galery, name='galery'),
    path('sales', views.sales, name='sales'),
    path('events', views.events, name='events'),
]