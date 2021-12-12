from django.shortcuts import render
from gifts.models import Gift
from .models import Countdown
from wishlists.models import Wishlist

def countdown(request):
    chosen_gifts = []
    gifts = Gift.objects.all()
    advent = Countdown.objects.first()
    wishlist = Wishlist.objects.filter(user=request.user).first()
    if wishlist.gifts:
        for gift in wishlist.gifts.all():
            chosen_gifts.append(gift.day)
            print("Hello World")


    context = {
        'gifts': gifts,
        'day': advent.day,
        'days_left': 10-advent.day,
        'chosen_gifts': chosen_gifts
    }
    return render(request, 'countdown/countdown.html', context)
