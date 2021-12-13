from django.shortcuts import render
from gifts.models import Gift
from .models import Countdown
from wishlists.models import Wishlist
from profiles.models import Profile

def countdown(request):
    chosen_gifts = []
    gifts = Gift.objects.all()
    advent = Countdown.objects.first()
    wishlist = Wishlist.objects.filter(user=request.user).first()
    profile = Profile.objects.filter(user=request.user).first()

    # if user doesnt have a wishlist, create it and save it to their profile
    if not wishlist:
        wishlist = Wishlist.objects.create(user=request.user)
        wishlist.save()

        profile.wishlist_owner = wishlist
        profile.save()
    
    # figure out which gifts are in wishlist
    if wishlist.gifts:
        for gift in wishlist.gifts.all():
            chosen_gifts.append(gift.day)

    context = {
        'gifts': gifts,
        'day': advent.day,
        'days_left': 10 - advent.day,
        'chosen_gifts': chosen_gifts
    }
    return render(request, 'countdown/countdown.html', context)
