from django.contrib.auth import logout
from django.shortcuts import redirect, render

from django.contrib import messages, auth

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
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('signin_user')
    context={}
    return render(request, 'accounts/signin_user.html', context)


def signout_user(request):
    auth.logout(request)
    messages.info(request, 'You are logged out')
    return redirect('signin_user')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
