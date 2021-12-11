from django.shortcuts import render
from gifts.models import Gift
from .models import Countdown

def countdown(request):
    gifts = Gift.objects.all()
    advent = Countdown.objects.first()
    context = {
        'gifts': gifts,
        'day': advent.day,
        'days_left': 10-advent.day
    }
    return render(request, 'countdown/countdown.html', context)
