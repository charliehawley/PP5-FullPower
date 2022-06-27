from django.shortcuts import render
from .models import Product

# Create your views here.
def products(request):
    render(request=Product)
    