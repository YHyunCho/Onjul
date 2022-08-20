from django.shortcuts import render

# Create your views here.
def landing(request):
  return render(
    request,
    'MainRefrigerator/landing.html',
  )

def index(request) :
  return render(
    request,
    'MainRefrigerator/index.html'
  )
