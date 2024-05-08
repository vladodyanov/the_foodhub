from django import forms
from the_foodhub.accounts.models import FoodHubUser, Profile
from the_foodhub.accounts.validators import allow_only_images_validator


class FoodHubUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = FoodHubUser
        fields = ('first_name', 'last_name', 'username', 'email', 'password')

    def clean(self):
        cleaned_data = super(FoodHubUserCreationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "Password does not match!"
            )


class FoodHubProfileForm(forms.ModelForm):
    profile_picture = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'btn.btn-info'}),
        validators=[allow_only_images_validator],
    )
    cover_photo = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'btn.btn-info'}),
        validators=[allow_only_images_validator],
    )

    class Meta:
        model = Profile
        fields = ("profile_picture", "cover_photo", "address_line_1", "address_line_2", "country", "region", "city",
                  "pin_code", "latitude", "longitude")
