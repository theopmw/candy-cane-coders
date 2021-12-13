from django.db import models
from gifts.models import Gift
from django.contrib.auth.models import User


class Wishlist(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, unique=False)
    gifts = models.ManyToManyField(Gift, blank=True, related_name='wishlist_gifts')

    def __str__(self):
        return f'{self.user.username}s wishlist gifts'
