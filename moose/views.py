from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.template import Context
from django.template.loader import get_template
from django.views.decorators.cache import cache_page #CACHE imports
from django.shortcuts import render_to_response
from django.contrib.sessions.models import Session
from django.contrib import auth
from django.contrib.auth.models import User
from moose.forms import *
from django.db import connection, transaction
import string,math
import re
from django.conf import settings

def _isValidLogin(request):
    password = request.POST.get('password', '')
    email = request.POST.get('email', '')
    user = auth.authenticate(email=email, password=password)
    if user is not None and user.is_active:
        return True
    else:
        return False

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            if _isValidLogin(request):
                return HttpResponseRedirect("get_deals")
    else:
        form = LoginForm()
    
    return render_to_response("login/login.html", {'form': form})

def newUser(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            username = request.POST.get('name', '')
            email = request.POST.get('email', '')
            password = request.POST.get('password', '')
            user = User.objects.create_user(username=username,email=email,password=password)
            user.save()
            return HttpResponseRedirect("get_deals")
    else:
        form = NewUserForm()
    return render_to_response("login/newuser.html", {'form': form})

def favorites(request):
    return render_to_response("favorites.html", {})

def deals(request):
    return render_to_response("deals.html", {})

def get_deals_json(request, *args, **kwargs):
    f = open(settings.BASE_DIR+'/moose/templates/deals_sample.json')
    l = f.readlines()
    f.close()
    return HttpResponse("".join(l), mimetype='application/json', status=200)
