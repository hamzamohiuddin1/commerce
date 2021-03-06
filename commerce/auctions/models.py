from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    watchlist = models.ManyToManyField(
        "Listings", blank=True, related_name="user_watch"
    )
    def __str__(self):
        return f"{self.username}"


class Listings(models.Model):
    ACTIVE = "ACTIVE"
    CLOSED = "CLOSED"
    product_name = models.CharField(max_length=64, default="")
    status = models.CharField(max_length=6, default="")
    id = models.IntegerField(primary_key=True, auto_created=True)
    starting_price = models.IntegerField()
    image_url = models.CharField(max_length=64, default="")
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_listings",default="")
    product_description = models.TextField(max_length = 512, default="")
    current_price = models.IntegerField(default=0)
    def updateCurrent(self):
        if self.bids:
            self.current_price = max(self.bids.get().amount)
        else:
            self.current_price = self.starting_price
    def __str__(self):
        return f"{self.product_name} Price: {self.current_price}"


class Bids(models.Model):
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE, related_name="bids")
    amount = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bidders")



class Comments(models.Model):
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE, related_name="listing_comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenters")
    content = models.CharField(max_length=256)


