from django.contrib import admin
from .models import Countdown


class CountdownAdmin(admin.ModelAdmin):
    fields = ('day', 'current_date', 'start_date', 'done')


admin.site.register(Countdown, CountdownAdmin)
