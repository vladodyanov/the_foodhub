from django.db import models

from the_foodhub.vendor.models import Vendor


class Category(models.Model):
    MAX_LENGHT_CATEGORY_NAME = 50
    MAX_LENGHT_SLUG = 100
    MAX_LENGHT_DESCRIPTION = 250

    vendor = models.ForeignKey(
        Vendor,
        on_delete=models.CASCADE
    )
    category_name = models.CharField(
        max_length=MAX_LENGHT_CATEGORY_NAME,
        unique=True
    )
    slug = models.SlugField(
        max_length=MAX_LENGHT_SLUG,
        unique=True
    )
    descriptions = models.TextField(
        max_length=MAX_LENGHT_DESCRIPTION,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.category_name
