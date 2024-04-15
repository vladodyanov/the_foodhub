from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views, logout
from django.urls import reverse_lazy, reverse
from django.views import generic as views


class SignInUserView(auth_views.LoginView):
    # template_name = 'accounts/signin_user.html'
    # redirect_authenticated_user = True
    # success_url = reverse_lazy('index')
    pass


class SignUpUserView(views.CreateView):
    # template_name = 'accounts/signup_user.html'
    # form_class = SpeachCenterUserCreationForm
    # queryset = Profile.objects.all()
    #
    # def get_success_url(self):
    #     return reverse('details profile', kwargs={'pk': self.object.pk})
    #
    # def form_valid(self, form):
    #     result = super().form_valid(form)
    #     login(self.request, form.instance)
    #     return result
    pass


def signout_user(request):
    logout(request)
    return redirect('index')