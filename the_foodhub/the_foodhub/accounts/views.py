from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views, logout, login
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from the_foodhub.accounts.forms import FoodHubUserCreationForm
from the_foodhub.accounts.models import Profile


class SignUpUserView(views.CreateView):
    template_name = 'accounts/signup_user.html'
    form_class = FoodHubUserCreationForm
    queryset = Profile.objects.all()
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, form.instance)
        return result


class SignInUserView(auth_views.LoginView):
    # template_name = 'accounts/signin_user.html'
    # redirect_authenticated_user = True
    # success_url = reverse_lazy('index')
    pass


def signout_user(request):
    logout(request)
    return redirect('index')