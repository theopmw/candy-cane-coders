from django.db import models
from gifts.models import Gift
from django.contrib.auth.models import User


class Wishlist(models.Model):
    item = models.ManyToManyField(Gift)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.item
