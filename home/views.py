from django.shortcuts import render
from products.models import Product
from music.models import Music

# Create your views here.


def index(request):
    """ Returns index page """

    merch = Product.objects.all()
    new_releases = Music.objects.filter(release_date__year=2022)

    context = {
        'merch': merch,
        'new_releases': new_releases
    }

    return render(request, 'home/index.html', context)
