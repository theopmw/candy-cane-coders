from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse

from wishlists.models import Wishlist
from gifts.models import Gift


def wishlists(request):
    wishlist = Wishlist.objects.filter(user=request.user).first()
    context = {'wishlist': wishlist}
    return render(request, "wishlists/wishlist.html", context)


@require_POST
def add_to_wishlist(request, gift_id):
    wishlist = Wishlist.objects.filter(user=request.user).first()
    gift = Gift.objects.get(pk=int(gift_id))
    wishlist.gifts.add(gift)
    return JsonResponse({'gift_id': gift_id})


@require_POST
def remove_from_wishlist(request, gift_id):
    gift = get_object_or_404(Gift, pk=gift_id)
    wishlist = Wishlist.objects.filter(user=request.user).first()
    wishlist.gifts.remove(gift)
    return JsonResponse({'gift_id': gift_id})