from django.shortcuts import render, redirect, reverse


def wishlists(request):
    context = {}
    template = "wishlists/wishlist.html"
    return render(request, template, context)


def add_to_wishlist(request, gift_id):
    return redirect(reverse("wishlists"))


def remove_from_wishlist(request, gift_id):
    return redirect(reverse("wishlists"))
