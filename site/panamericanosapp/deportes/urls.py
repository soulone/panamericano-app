from django.urls import path
from . import views

app_name= 'deportes'

urlpatterns = [
     path('',views.index, name = 'index'),
]