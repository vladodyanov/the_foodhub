from django.contrib import admin

from the_foodhub.vendor.models import Vendor


@admin.register(Vendor)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_profile', 'vendor_name', 'vendor_license', 'is_approved', 'created_at', 'modified_at')
