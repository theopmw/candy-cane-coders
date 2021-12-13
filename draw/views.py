from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from random import randint
from datetime import datetime, timedelta
import string    
import random

from profiles.models import Profile
from wishlists.models import Wishlist
from countdown.models import Countdown
from gifts.models import Gift


@require_POST
def increase_day(request):
    if request.user.is_superuser:
        countdown = Countdown.objects.first()
        if countdown.day <= 10:
            countdown.day += 1
            countdown.save()
            return JsonResponse({'status': 200})
        else:
            return JsonResponse({'status': 406, 'message': 'Cannot increase day any more.'}) 
    else: 
        return JsonResponse({'status': 401})

@require_POST
def set_day_11(request):
    if request.user.is_superuser:
        countdown = Countdown.objects.first()
        countdown.day = 11
        countdown.current_date = countdown.start_date + timedelta(days=10)
        countdown.done = False
        countdown.save()
        return JsonResponse({'status': 200})
    else: 
        return JsonResponse({'status': 401})

@require_POST
def reset_draw(request):
    if request.user.is_superuser:
        # reset countdown
        countdown = Countdown.objects.first()
        countdown.day = 1
        countdown.current_date = datetime.now()
        countdown.start_date = datetime.now()
        countdown.done = False
        countdown.save()

        # reset profiles / wishlists
        profiles = Profile.objects.all()
        for profile in profiles:
            profile.wishlist_sender = None
            profile.gift_given = None
            profile.gift_received = None
            profile.save()

        return JsonResponse({'status': 200})
    else: 
        return JsonResponse({'status': 401})


def create_draw(request):
    print("Draw Created")
    # end countdown
    countdown = Countdown.objects.first()
    countdown.day = 11
    countdown.current_date = countdown.start_date + timedelta(days=10)
    countdown.done = True
    countdown.save()

    # reset wishlists in case any are there
    profiles = Profile.objects.all()
    for profile in profiles:
        profile.wishlist_sender = None
        profile.gift_given = None
        profile.gift_received = None
        profile.save()

    # get all wishlists and profiles
    wishlists = [wishlist for wishlist in Wishlist.objects.all()]
    profiles = [profile for profile in Profile.objects.all()]

    # if odd number of users - exclude admin
    if len(profiles) % 2 == 1:
        wishlists = [wishlist for wishlist in Wishlist.objects.all() if wishlist.user.username != 'admin']
        profiles = [profile for profile in Profile.objects.all() if profile.user.username != 'admin']

    # for each profile - assign a random wishlist
    for profile in profiles:
        random_wishlist_index = 0
        random_wishlist = None

        while True:
            random_wishlist_index = randint(0, len(wishlists) - 1)
            random_wishlist = wishlists[random_wishlist_index]
            if random_wishlist.user.username != profile.user.username:
                break

        # if the wishlist is empty - add all gifts
        if random_wishlist.gifts.all().count() == 0:
            for gift in Gift.objects.all():
                random_wishlist.gifts.add(gift)
                random_wishlist.save()
        
        profile.wishlist_sender = random_wishlist
        profile.save()

        del wishlists[random_wishlist_index]

