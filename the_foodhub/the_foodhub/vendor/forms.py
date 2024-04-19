from django import forms
from the_foodhub.vendor.models import Vendor


class FoodHubVendorCreationForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ("vendor_name", "vendor_license")
