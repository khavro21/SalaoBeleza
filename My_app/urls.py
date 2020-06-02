from django.contrib import admin
from django.urls import path
from . import views
from .views import PostListView
urlpatterns = [

    path('', views.index, name='home'),
    path('contacts', views.contacts, name='contacts'),
    path('about', views.about, name='about'),
    path('services', PostListView.as_view(), name='services'),
    path('galery', views.galery, name='galery'),
    path('specialists', views.specialists, name='galery'),
    path('sales', views.sales, name='sales'),
    path('events', views.events, name='events'),
]