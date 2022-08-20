from django.shortcuts import render
from django.views.generic import ListView
from .models import SharingList

# Create your views here.
def index(request) :
  return render(
    request,
    'sharing/index.html',
  )