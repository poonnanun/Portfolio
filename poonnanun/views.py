from django.shortcuts import render
from poonnanun.models import Contact

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'index.html')
