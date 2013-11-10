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
    import ipdb
    ipdb.set_trace()
    password = request.POST.get('password', '')
    username = request.POST.get('name', '')
    user = auth.authenticate(username=username, password=password)

    #Don't try this at home... or anywhere
    #import ipdb
    #ipdb.set_trace()
    #request.session['email'] = form.email
    #request.session['password'] = request.GET['password']

    if user is not None and user.is_active:
        return True
    else:
        return False

def login(request):
    #import ipdb
    #ipdb.set_trace()
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
            #Don't try this at home... or anywhere
            #import ipdb
            #ipdb.set_trace()
            request.session['email'] = email
            request.session['password'] = password

            return HttpResponseRedirect("get_deals")
    else:
        form = NewUserForm()
    return render_to_response("login/newuser.html", {'form': form})

def favorites(request):
    return render_to_response("favorites.html", {})

def deals(request):
    return render_to_response("deals.html", {})

def fav_json(request):
    return render_to_response("../static/fav.json", {})

def set_favorite(request, id, value):
    fav = Favorite(email=id, isFavorite=(True if value.lower() == 'true' else False))
    fav.save()
    return HttpResponse(s(str(email))

def get_deals_json(request, *args, **kwargs):
    
    f = open(settings.BASE_DIR+'/moose/templates/deals_sample.json')
    l = f.readlines()
    f.close()
    return HttpResponse(request.session.email, mimetype='application/json', status=200)
        #"".join(l), mimetype='application/json', status=200)
