from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'gnrtr/home.html')

def eggs(request):
    return HttpResponse('<h1>Яйцо</h1>')

def hp(request):
    return render(request, 'gnrtr/hp.html')

def about(request):
    return render(request, 'gnrtr/about.html')

def password(request):

    #thepass = 'testing'
    char = list('qwertyuiopasdfghjklzxcvbnm')
    if request.GET.get('uppercase'):
        char.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))

    if request.GET.get('special'):
        char.extend(list('!@#$%^&*(){}'))

    if request.GET.get('numbers'):
        char.extend(list('1234567890'))

    length = int(request.GET.get('length'),10)

    thepass = ''
    for x in range(length):
        thepass += random.choice(char)

    return render(request, 'gnrtr/pass.html', {'password':thepass})
