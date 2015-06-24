from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
home_page = None

def home_page(request):
    return HttpResponse('<html><title>Python.pro.br: Catálogo de cursos</title></html>')
