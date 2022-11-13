from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('jet/',include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('',views.index),
    path('about/',include('about.urls')),
    path('buku/',include ('buku.urls')),
     path('tamu/',include ('tamu.urls')),
]
