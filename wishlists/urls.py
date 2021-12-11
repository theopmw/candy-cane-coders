from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', login_required(views.wishlists), name='wishlists'),
    path('add_to_wishlist/<int:gift_id>', login_required(views.add_to_wishlist), name='add_to_wishlist'),
    path('remove_from_wishlist/<int:gift_id>',login_required(views.remove_from_wishlist), name='remove_from_wishlist'),
]
