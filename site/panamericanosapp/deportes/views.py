from django.template import loader
from django.shortcuts import render
from .models import Deporte
from django.utils import timezone
from django.http import HttpResponse
from django.http import Http404


def index(request):
    deportes=Deporte.objects.all()
    return render(request, 'deportes/index.html',{'deportes':deportes})

