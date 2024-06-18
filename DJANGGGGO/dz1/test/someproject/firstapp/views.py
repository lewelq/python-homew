from django.shortcuts import render
from django.http import HttpResponse
from random import randint

# Create your views here.

def index(request):
    return HttpResponse('hello world')

def orel_reshka(request):
    return HttpResponse(f'{randint(1, 2)}')

def cube(request):
    return HttpResponse(f'{randint(1, 6)}')

def number(request):
    return HttpResponse(f'{randint(1, 100)}')