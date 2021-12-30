from django.contrib import admin

from .models import Bids, Listings, User, Comments
# Register your models here.
admin.site.register(Bids)
admin.site.register(Listings)
admin.site.register(User)
admin.site.register(Comments)