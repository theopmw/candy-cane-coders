from django.urls import path
from . import views

urlpatterns = [
    path("", views.wishlists, name="wishlists"),
    path("add_to_wishlist/<gift_name>", views.add_to_wishlist, name="add_to_wishlist"),
    path(
        "remove_from_wishlist/<gift_name>",
        views.remove_from_wishlist,
        name="remove_from_wishlist",
    ),
]
