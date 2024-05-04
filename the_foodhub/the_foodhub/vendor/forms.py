from django import forms
from the_foodhub.vendor.models import Vendor


class FoodHubVendorCreationForm(forms.ModelForm):
    vendor_license = forms.ImageField(widget=forms.FileInput(attrs={'class': 'btn.btn-info'}))
    class Meta:
        model = Vendor
        fields = ("vendor_name", "vendor_license")
