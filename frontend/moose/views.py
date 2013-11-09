# Create your views here.
from django.http import HttpRequest
from django.shortcuts import render_to_response
#from garden.light.form import *
#from garden.light.models import *

def hello(request):
    return HttpRequest("test of the emergency broadcast system")

# Create your views here.
