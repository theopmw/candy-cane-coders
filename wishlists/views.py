from django.shortcuts import render, redirect


def wishlists(request):
    context = {}
    template = "wishlists/wishlist.html"
    return render(request, template, context)


def add_to_wishlist(request):
    return redirect("wishlists/")


def remove_from_wishliast(request):
    return redirect("wishlists/")
