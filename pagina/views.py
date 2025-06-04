from django.shortcuts import render
from django.http import HttpResponse
from .models import Publicacion
# Create your views here.

def home(request):
    publicacion = Publicacion.objects.all()
    return render(request, 'home.html',{'publicacion':publicacion})