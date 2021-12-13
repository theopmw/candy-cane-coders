from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('user',)
    fields = ('full_name', 'wishlist_owner', 'wishlist_sender', 'gift_given', 'gift_received',)


admin.site.register(Profile, ProfileAdmin)

