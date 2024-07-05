from urllib.request import Request
from wsgiref.util import request_uri
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import login
from django.contrib import messages
from .models import Feature
from .forms import signupForm
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,logout
import datetime
from typing import Dict, List
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.urls import reverse_lazy
from django.views.generic import (DeleteView, ListView, TemplateView,UpdateView, View)
# from formtools.wizard.views import SessionWizardView
# from booking.forms import (BookingCustomerForm, BookingDateForm, BookingSettingsForm, BookingTimeForm)
# from booking.models import Booking, BookingSettings
# from booking.settings import (BOOKING_BG, BOOKING_DESC, BOOKING_DISABLE_URL,BOOKING_SUCCESS_REDIRECT_URL, BOOKING_TITLE,PAGINATION)
# from booking.utils import BookingSettingMixin


def index(request):
    return render(request, 'index.html')


def tst(request):
    features = Feature.objects.all()
    return render(request, 'tst.html', { 'feature': features})



def signup(request):
    if request.method=='POST':
        form=signupForm(request.POST)
        form = signupForm(request.POST)
        if form.is_valid():
            firstname=form.cleaned_data['name']
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=User.objects.create_user(username, password=password)
            user.first_name=firstname
            user.save()
            login(request, user)
            return redirect('/')
    return render(request,'signup.html')

def gallery(request):
    return render(request, 'gallery.html')

def signin(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request, user)
            return redirect('/')
    return render(request, 'signin.html')



def signout(request):
    if request.method=='POST':
        logout(request)
        #return redirect('/')
        return redirect('/')

    return render(request, 'logout.html')


def reservation(request):
    return render(request, 'reservation.html')

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        PhoneNum = request.POST['PhoneNum']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password2 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used.')
                return redirect('')
            elif User.objects.filter(PhoneNum = PhoneNum).exists():
                messages.info(request, 'Phonr Number Already used')
                return redirect('')
            else:
                User.objects.create_user(username = username, email = email, password = password, PhoneNum = PhoneNum)
                User.save()
                return redirect('login')
        else:
            messages.info(request, 'Wrong password')
            return redirect('')
    else:
        return render(request, 'register.html')


def contact(request):
    return render(request, 'contact.html')

def outdoor(request):
    return render(request, 'outdoor.html')

def other(request):
    return render(request, 'other.html')

def video(request):
        return render(request, 'video.html')

def advertising(request):
        return render(request, 'advertising.html')

def other2(request):
         return render(request, 'other2.html')


def reservation2(request, year, month):
    month = month.capitalize()
    # features = Feature.objects.all()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    cal = HTMLCalendar().formatmonth(year, month_number)
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%I:%M:%S %p')
    return render(request, 'reservation2.html', {
        "year": year,
        "month": month,
        "month_number": month_number,
        "cal": cal,
        "current_year": current_year,
        "time": time,
    })