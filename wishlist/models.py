from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from products.models import Product
from profiles.models import UserProfile


class wishlist(models.Model):
    """ Model for maintaining a wishlist """

    user = models.ForeignKey(UserProfile, null=False, blank=False,
                             on_delete=models.CASCADE,
                             related_name='wishlist')
    products = models.ManyToManyField(Product, through='WishlistItem')

    def __str__(self):
        return f'Wishlist ({self.user})'


@receiver(post_save, sender=UserProfile)
def create_or_update_user_wishlist(sender, instance, created, **kwargs):
    """
    Create wishlist when user signs up
    """
    if created:
        Wishlist.objects.create(user=instance)