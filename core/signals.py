from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile_if_missing(sender, instance, created, **kwargs):
    """
    Safety net: ensures every User has a Profile, even if created outside
    the signup form (e.g. via createsuperuser or the admin panel).
    """
    if created:
        Profile.objects.get_or_create(user=instance)
