import csv, io
#from django.contrib.auth.decorations import permisions_required
from django.shortcuts import render
from .models import Product
from django.http import HttpResponse

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products':products})
