from django.db import models

from the_foodhub.accounts.models import FoodHubUser, Profile


class Vendor(models.Model):
    MAX_VENDOR_NAME_LENGTH = 50

    user = models.OneToOneField(
        FoodHubUser,
        related_name='user',
        on_delete=models.CASCADE,
    )

    user_profile = models.OneToOneField(
        Profile,
        related_name='user_profile',
        on_delete=models.CASCADE,
    )

    vendor_name = models.CharField(
        max_length=MAX_VENDOR_NAME_LENGTH,
    )

    vendor_license = models.ImageField(
        upload_to='vendor/licence',
    )

    is_approved = models.BooleanField(
        default=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    modified_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.vendor_name
