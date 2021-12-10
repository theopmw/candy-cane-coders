from django.db import models
from gifts.models import Gift


class Wishlist(models.Model):
    item = models.ManyToManyField(Gift)

    def __str__(self):
        return self.item
