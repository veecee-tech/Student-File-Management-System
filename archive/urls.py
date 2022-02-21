from django.urls import path 
from .views import *


urlpatterns = [
    path('', archive_home, name='archive_home'),
    path('search/', search_archive, name="search-archive"),
    path('record/<int:pk>', alumni_document, name='alumni-document')
]

