
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from . import views



urlpatterns = [
    
    path('admin/', admin.site.urls, name='admin'),
    path('', views.index, name='home'),
    path('auth/', include('authentication.urls')),
    path('adviser/', include('level_adviser.urls')),
    path('student/', include('student.urls')),
    path('archive/', include('archive.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
