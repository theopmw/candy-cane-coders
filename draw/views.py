from django.shortcuts import render
from random import randint

from profiles.models import Profile
from wishlists.models import Wishlist
from countdown.models import Countdown

def increase_day(request):
    pass

def create_draw(request):
    countdown = Countdown.objects.first()
    wishlists = [wishlist for wishlist in Wishlist.objects.all()]
    profiles = [profile for profile in Profile.objects.all()]
    odd_or_even = 0 if len(profiles) % 2 else 1

    while len(profiles) > 0:
        # get random wishlist index and profile index
        rand_profile_index = randint(0, len(profiles) - 1)
        rand_wishlist_index = randint(0, len(wishlists) - 1)

        # get random wishlist and profile
        rand_profile = profiles[rand_profile_index]
        rand_wishlist = wishlists[rand_wishlist_index]

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


