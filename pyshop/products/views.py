from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import Product
# Create your views here.


def index(request):
    products = Product.objects.all()
    # Product.objects.filter()
    # Product.objects.get()
    # Product.objects.save()
    return render(request, "index.html", {"products": products})


def new(requests):
    return HttpResponse('New Products Brian')
