from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing_page", views.create_listing_page, name="create_listing_page"),
    path("new_listing", views.new_listing, name="new_listing"),
    path("<int:id>", views.listing, name="listing")
]
