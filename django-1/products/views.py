from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def sayhi(request):
    return HttpResponse('hello world')