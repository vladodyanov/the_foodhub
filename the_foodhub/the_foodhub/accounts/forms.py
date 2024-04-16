from django.contrib.auth import forms as auth_forms

from the_foodhub.accounts.models import FoodHubUser


class FoodHubUserCreationForm(auth_forms.UserCreationForm):

    class Meta(auth_forms.UserCreationForm.Meta):
        model = FoodHubUser
        fields = ('first_name','last_name', 'username', 'email', 'phone_number', 'password')

    def save(self, *args, **kwargs):
        self.user = super().save(*args, **kwargs)
        return self.user