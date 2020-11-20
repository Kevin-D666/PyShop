from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import Product
# Create your views here.


def index(requests):
    products = Product.objects.all()
    # Product.objects.filter()
    # Product.objects.get()
    # Product.objects.save()
    return HttpResponse('Hello Brian')


def new(requests):
    return HttpResponse('New Products Brian')
