
from django.contrib.auth import  logout
from django.shortcuts import redirect, render

from django.contrib import messages

from the_foodhub.accounts.forms import FoodHubUserCreationForm
from the_foodhub.accounts.models import FoodHubUser


def signup_user(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in!')
        return redirect('home')
    elif request.method == 'POST':
        form = FoodHubUserCreationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = FoodHubUser.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                                   email=email, password=password)
            user.role = FoodHubUser.CUSTOMER
            user.save()

            # # Send verification email
            # mail_subject = 'Please activate your account'
            # email_template = 'accounts/emails/account_verification_email.html'
            # send_verification_email(request, user, mail_subject, email_template)
            messages.success(request, 'Your account has been registered successfully!')
            return redirect('signup_user')
        else:
            print('invalid form')
            print(form.errors)
    else:
        form = FoodHubUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup_user.html', context)


def signin_user(request):
    pass


def signout_user(request):
    logout(request)
    return redirect('index')
