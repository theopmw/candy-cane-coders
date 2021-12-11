from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from .models import Profile
from wishlists.models import Wishlist


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        wishlist = Wishlist.objects.create(user=instance)
        Profile.objects.create(user=instance, wishlist_owner=wishlist)
    instance.profile.save()