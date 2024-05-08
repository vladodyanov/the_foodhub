from django import forms

from the_foodhub.accounts.validators import allow_only_images_validator
from the_foodhub.vendor.models import Vendor


class FoodHubVendorCreationForm(forms.ModelForm):
    vendor_license = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'btn btn-info'}),
        validators=[allow_only_images_validator],
    )

    class Meta:
        model = Vendor
        fields = ("vendor_name", "vendor_license")
