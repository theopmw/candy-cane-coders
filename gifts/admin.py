from django.contrib import admin
from .models import Gift


class GiftAdmin(admin.ModelAdmin):
    fields = ('name', 'image', 'day')


admin.site.register(Gift, GiftAdmin)
