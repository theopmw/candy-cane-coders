from django.shortcuts import render, redirect, reverse
from django.views.decorators.http import require_POST
from django.http import JsonResponse


def wishlists(request):
    context = {}
    template = "wishlists/wishlist.html"
    return render(request, template, context)

@require_POST
def add_to_wishlist(request, gift_id):
    # get the gift based on its id and add to the users wishlist
    if request.method == 'POST':
        print("GIFT_ID = ", int(gift_id))
        return JsonResponse({'gift_id': gift_id})

    return redirect(reverse("wishlists"))

@require_POST
def remove_from_wishlist(request, gift_id):
    return redirect(reverse("wishlists"))
