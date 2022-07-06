from django.shortcuts import render, redirect
# from products.models import Product

# Create your views here.

def view_bag(request):
    """ Returns bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, product.id):
    """ Adds product to bag context """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag