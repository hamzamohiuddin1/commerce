from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import User, Listings, Bids, Comments
from django import forms
from django.contrib.auth.decorators import login_required


class NewListingForm(forms.Form):
    product_name = forms.CharField(max_length=64, label="Product Name")
    product_description = forms.CharField(label="Description", widget=forms.Textarea)
    starting_price = forms.IntegerField(label="Starting Price")
    image_url = forms.URLField(max_length=64, label="Image Url", required=False)

class BidForm(forms.Form):
    bid_amount = forms.IntegerField(min_value=0, label="Bid Amount", required=False)


def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listings.objects.filter(status="ACTIVE").all()
    })

def listing(request, id):
    listing = Listings.objects.filter(pk=id)[0]
    return render(request, "auctions/listing.html",{
        "id": id,
        "listing": Listings.objects.filter(pk=id)[0],
        "bidForm": BidForm(),
        "product_name": listing.product_name,
        "status": listing.status,
        "starting_price": listing.starting_price,
        "image_url": listing.image_url,
        "seller": listing.seller,
        "product_description": listing.product_description

    })

@login_required(login_url="/login")
def create_listing_page(request):
    return render(request, "auctions/create_listing_page.html",{
        "form": NewListingForm()
    })


def new_listing(request):
    if request.method == "POST":
        product_name = request.POST["product_name"]
        product_description = request.POST["product_description"]
        starting_price = request.POST["starting_price"]
        image_url = request.POST["image_url"]
        status = Listings.ACTIVE
        seller = request.user

        listing = Listings(product_name=product_name, product_description = product_description,
                          starting_price=starting_price, image_url=image_url, status=status, seller=seller)
        listing.save()
        return HttpResponseRedirect(reverse("index"))




    pass


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
