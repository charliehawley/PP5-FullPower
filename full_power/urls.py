from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('music/', include('music.urls')),
    path('bag/', include('bag.urls')),
    path('favicon.ico',
         RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico'))),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
