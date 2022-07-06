from django.shortcuts import render
# from products.models import Product

# Create your views here.

def view_bag(request):
    """ Returns bag contents page """

    return render(request, 'bag/bag.html')
