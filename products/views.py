from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Band

# Create your views here.
def product_details(request, product_id):
    """ Returns product details page """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product
    }

    return render(request, 'products/product-details.html', context)

def all_products(request):
    """ Returns products page """

    products = Product.objects.all()
    query = None
    category = None
    band = None

    if request.GET:
        if 'band' in request.GET:
            band = request.GET['band'].split(',')
            products = products.filter(band__name__in=band)
            band = Band.objects.filter(name__in=band)

    if request.GET:
        if 'category' in request.GET:
            category = request.GET['category'].split(',')
            products = products.filter(category__name__in=category)
            category = Category.objects.filter(name__in=category)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You haven't entered any search terms!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': category,
    }

    return render(request, 'products/products.html', context)
