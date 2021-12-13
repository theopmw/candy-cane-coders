from django.shortcuts import render, redirect, reverse
from django.views.decorators.http import require_POST
from django.http import JsonResponse

from profiles.models import Profile
from .models import Gift
from countdown.models import Countdown

def gift_given(request):
    context = {
        'gift': None,
        'wishlist': None,
        'sent': False,
        'days_left': 0
    }

    wishlist = Profile.objects.get(user=request.user)
    countdown = Countdown.objects.all().first()
    context['days_left'] = 10 - countdown.day 
    context['wishlist'] = wishlist.wishlist_sender

    if context['days_left'] <= 0: 
        context['days_left'] = 0
    
    if wishlist.gift_given:
        context['gift'] = wishlist.gift_given
        context['sent'] = True

    return render(request, 'gifts/gift_given.html', context)


def gift_received(request):
    context = {
        'gift': None,
        'days_left': 0
    }

    wishlist = Profile.objects.get(user=request.user)
    countdown = Countdown.objects.all().first()
    context['days_left'] = 10 - countdown.day
   
    if context['days_left'] <= 0: 
        context['days_left'] = 0

    if wishlist.wishlist_sender:
        context['gift_sender'] = wishlist.wishlist_sender.user.username
    
    if wishlist.gift_received:
        context['gift'] = wishlist.gift_received

    return render(request, 'gifts/gift_received.html', context)


@require_POST
def gift_send(request, gift_id, user_id):
    user_giving = Profile.objects.get(user=request.user)
    user_receiving = Profile.objects.get(pk=user_id)
    gift = Gift.objects.get(pk=gift_id)

    user_giving.gift_given = gift
    user_receiving.gift_received = gift

    user_giving.save()
    user_receiving.save()
    
    return JsonResponse({"ok": 200})