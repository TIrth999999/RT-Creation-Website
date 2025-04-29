# MODEL IMPORT
from app.models import *

from django.shortcuts import render

# MESSAGES AND SHORTCUT IMPORT
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect

# AUTHENTICATION IMPORT
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# THIRD PARTY AND OTHER NECCESARRY UTILITY IMPORT
import yt_dlp
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
import os
from django.conf import settings
from django.http import FileResponse

def index(request):
    counter, created = VisitorCounter.objects.get_or_create(id=1)
    
    if request.method == "POST":
        counter.count += 1
        counter.save()
        return redirect("home")

    if not request.session.get('has_visited'):
        counter.count += 1
        counter.save()
        request.session['has_visited'] = True

    return render(request,'index.html',{'counter': counter})

def review(request):

    reviews = Reviews.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        rating = request.POST.get('rating')
        review = Reviews(name=name, email=email, desc=desc, rating=rating)
        review.save()

    return render(request,'review.html',{'reviews': reviews})

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = request.POST.get('contact')
        contactObj = Contact(name=name, email=email, desc=desc, contact=contact)
        contactObj.save()

    return render(request,'contact.html')