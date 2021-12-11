from django.contrib import admin
from .models import Wishlist


class WishlistAdmin(admin.ModelAdmin):
    read_only_fields = ('user',)
    fields = ('user', 'gifts',)


admin.site.register(Wishlist, WishlistAdmin)
