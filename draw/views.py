from django.shortcuts import render
from django.http import JsonResponse
from random import randint

from profiles.models import Profile
from wishlists.models import Wishlist
from countdown.models import Countdown

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

def set_day_11(request):
    if request.user.is_superuser:
        countdown = Countdown.objects.first()
        day = countdown.day
        countdown.day = 11
        countdown.save()
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

        # assign wishlist to profile
        rand_profile.wishlist_sender = rand_wishlist
        rand_profile.save()

        # del profile and wishlist from lists
        del profiles[rand_profile_index]
        del wishlists[rand_wishlist_index]

    countdown.done = True
    countdown.save()


