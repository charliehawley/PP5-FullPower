from django.shortcuts import render
from .models import Music

# Create your views here.
def all_music(request):
    """ Returns products page """

    music = Music.objects.all()

    context = {
        'music': music,
    }

    return render(request, 'music/music.html', context)
