from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.


def index(requests):
    return HttpResponse('Hello Brian')


def new(requests):
    return HttpResponse('New Products Brian')
