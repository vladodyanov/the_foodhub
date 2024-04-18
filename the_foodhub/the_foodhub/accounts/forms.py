from django.contrib.auth import forms as auth_forms
from django import forms

from the_foodhub.accounts.models import FoodHubUser


class FoodHubUserCreationForm(auth_forms.UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta(auth_forms.UserCreationForm.Meta):
        model = FoodHubUser
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


    def save(self, *args, **kwargs):
        self.user = super().save(*args, **kwargs)
        return self.user