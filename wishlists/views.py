from django.shortcuts import render


def wishlists(request):
    context = {}
    return render(request, "wishlists/wishlist.html", context)
