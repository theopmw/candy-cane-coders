from django.urls import path
from . import views

urlpatterns = [
    path("", views.wishlists, name="wishlists"),
    path(
        "add_to_wishlist/<gift_name>", views.add_to_wishlists, name="add_to_wishlists"
    ),
]
