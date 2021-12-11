from django.db import models
from django.contrib.auth.models import User
from gifts.models import Gift

from wishlists.models import Wishlist

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200, blank=True, null=True)
    wishlist_owner = models.OneToOneField(Wishlist, null=True, blank=True, on_delete=models.SET_NULL, related_name="wishlist_owner")
    wishlist_sender = models.OneToOneField(Wishlist, null=True, blank=True, on_delete=models.SET_NULL, related_name="wishlist_sender")
    gift_given = models.OneToOneField(Gift, null=True, blank=True, on_delete=models.SET_NULL, related_name="gift_given")
    gift_received = models.OneToOneField(Gift, null=True, blank=True, on_delete=models.SET_NULL, related_name="gift_received")

    def __str__(self):
        return self.user.username
