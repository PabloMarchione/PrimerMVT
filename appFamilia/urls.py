from django.urls import path
from .views import *

urlpatterns = [
    path("padre/", Padre),
    path("madre/", madre),
    path("hijo/", hijo),
]
