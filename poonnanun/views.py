from django.shortcuts import render, get_object_or_404
from poonnanun.models import Contact

def index(request):
    return render(request, 'index.html')

def contact(request):

    return render(request, 'contact.html')
