from django.urls import path
from . import views

urlpatterns= [
    path("", views.index, name="index"),
    path("hamza", views.hamza, name="hamza"),
    path("<str:name>", views.greet, name="greet"),
    path("isitchristmas", views.isitchristmas, name="isitchristmas")
]