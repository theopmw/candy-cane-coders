from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from random import randint
from datetime import datetime, timedelta

from profiles.models import Profile
from wishlists.models import Wishlist
from countdown.models import Countdown
from gifts.models import Gift

@require_POST
def increase_day(request):
    if request.user.is_superuser:
        countdown = Countdown.objects.first()
        day = countdown.day
        if day <= 10:
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
        profiles = Profile.objects.all()

        for profile in profiles:
            profile.wishlist_sender = None
            profile.gift_given = None
            profile.gift_received = None
            profile.save()

        day = countdown.day
        countdown.day = 11
        countdown.done = False
        countdown.save()

        return JsonResponse({'status': 200})
    else:
        return JsonResponse({'status': 401})


@require_POST
def reset_draw(request):
    if request.user.is_superuser:
        countdown = Countdown.objects.first()
        profiles = Profile.objects.all()

        countdown.day = 1
        countdown.done = False
        countdown.start_date = datetime.now()
        countdown.current_date = datetime.now()
        countdown.save()

        for profile in profiles:
            profile.wishlist_sender = None
            profile.gift_given = None
            profile.gift_received = None
            profile.save()

        return JsonResponse({'status': 200})
    else:
        return JsonResponse({'status': 401})


def create_draw(request):
    countdown = Countdown.objects.first()
    wishlists = [wishlist for wishlist in Wishlist.objects.all()]
    profiles = [profile for profile in Profile.objects.all()]
    odd_or_even = len(profiles) % 2 # 0 == even, 1 == odd

    while len(profiles) > 0:
        # get random wishlist index and profile index
        rand_profile_index = randint(0, len(profiles) - 1)
        rand_wishlist_index = randint(0, len(wishlists) - 1)

        # get random wishlist and profile
        rand_profile = profiles[rand_profile_index]
        rand_wishlist = wishlists[rand_wishlist_index]

        # check that we are not sening gift list to same profile
        if rand_profile.user.username == rand_wishlist.user.username:
            continue

        # if an odd number of user, delete the admin
        if odd_or_even == 1:
            if rand_profile.user.username == 'admin':
                del profiles[rand_profile_index]
                odd_or_even = 0
                continue

        # if the wishlist is empty - add all items
        if rand_wishlist.gifts.all().count() == 0:
            for gift in Gift.objects.all():
                rand_wishlist.gifts.add(gift)
                rand_wishlist.gifts.save()
                rand_wishlist.save()

        # assign wishlist to profile
        rand_profile.wishlist_sender = rand_wishlist
        rand_profile.save()

        # del profile and wishlist from lists
        del profiles[rand_profile_index]
        del wishlists[rand_wishlist_index]

    countdown.done = True
    countdown.save()


