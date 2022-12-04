from account.models import User, UserWishList
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

@receiver(post_save, sender=User)
def user_wish_list(sender, instance, created, **kwargs):
    if created:
        user = instance
        user_wish_list = UserWishList.objects.create(user=user)
        user_wish_list.wish_list.add()
        user_wish_list.save()