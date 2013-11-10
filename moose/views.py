from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.template import Context
from django.template.loader import get_template
from django.views.decorators.cache import cache_page #CACHE imports
#from vBVS.FrontEnd.models import Run,Resource,Runplan,Buildsready
#from vBVS.FrontEnd.models import Baselineinfo,User,Notification,Notificationlist
from django.shortcuts import render_to_response
from moose.forms import *
from django.db import connection, transaction
import string,math
import re

def _isValidEmail(request):
    return True

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            if _isValidEmail(request):
                return HttpResponseRedirect("get_deals")
    else:
        form = LoginForm()
    
    return render_to_response("login/login.html", {'form': form})

def test1(request, *args, **kwargs):
    import ipdb
    #ipdb.set_trace()
    return HttpResponse("args: %s, kwargs: %s, session: %s"%\
                            (args, kwargs, type(request.session))
                        , status=200)

def home(request, *args, **kwargs):
    import ipdb
    #ipdb.set_trace()
    return HttpResponse("args: %s, kwargs: %s, session: %s"%\
                            (args, kwargs, type(request.session))
                        , status=200)

def deals(request):
    return render_to_response("deals.html", {})
