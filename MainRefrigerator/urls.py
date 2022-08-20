from django.urls import path, include
from . import views

app_name = 'Refrigerator' 

urlpatterns = [
  path('index/', views.index),
  path('', views.landing),

]