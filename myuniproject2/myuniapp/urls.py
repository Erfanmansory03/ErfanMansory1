from os import name
from django.urls import path
from . import views
from datetime import date
from django.http import HttpResponse
from django.shortcuts import render
#from djreservation import urls as djreservation_urls

urlpatterns = [
    path('', views.index, name = 'index'),
    #path('tst/', views.tst, name = "tst"),
    path('reservation/', views.reservation, name = "reservation"),
    path('register/', views.register, name = 'register'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/',views.signout,name='logout'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact', views.contact, name = 'contact'),
    path('outdoor', views.outdoor, name = 'outdoor'),
    path('other', views.other, name = 'other'),
    path('video', views.video, name = 'video'),
    path('advertising', views.advertising, name = 'advertising'),
    path('other2', views.other2, name = 'other2'),
    path('<int:year>/<str:month>/', views.reservation2, name = "reservation2"),

]
#path converters
#int: numbers
#str: strings
#path: whole urls/
#slugs: hyphen-and_underscores_stuff
#UUID: universally unique identifier
