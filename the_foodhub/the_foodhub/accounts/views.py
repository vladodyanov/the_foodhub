from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.utils.http import urlsafe_base64_decode

from the_foodhub.accounts.forms import FoodHubUserCreationForm
from the_foodhub.accounts.models import FoodHubUser
from the_foodhub.accounts.utils import (detect_user, check_role_customer, send_verification_email)


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = FoodHubUser._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, FoodHubUser.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulations! Your account is activated')
        return redirect('my_account')
    else:
        messages.error(request, 'Invalid activation link')
        return redirect('my_account')


def forgot_password(request):
    if request.method == 'POST':
        email = request.POST['email']

        if FoodHubUser.objects.filter(email=email).exists():
            user = FoodHubUser.objects.get(email__exact=email)

            mail_subject = 'Please reset your password'
            email_template = 'accounts/emails/reset_password_email.html'
            send_verification_email(request, user, mail_subject, email_template)
            messages.success(request, 'Password reset link was send to your email address.')
            return redirect('signin_user')
        else:
            messages.error(request, 'This account does not exist')
            return redirect('forgot_password')

    return render(request, 'accounts/forgot_password.html')


def reset_password_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = FoodHubUser._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, FoodHubUser.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.info(request, 'Please reset your password')
        return redirect('reset_password')
    else:
        messages.error(request, 'This link has been expired!')
        return redirect('my_account')


def reset_password(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            pk = request.session.get('uid')
            user = FoodHubUser.objects.get(pk=pk)
            user.set_password(password)
            user.is_active = True
            user.save()
            messages.success(request, 'Password reset successful')
            return redirect('signin_user')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('reset_password')

    return render(request, 'accounts/reset_password.html')


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

            # Send verification email
            mail_subject = 'Please activate your account'
            email_template = 'accounts/emails/account_verification_email.html'
            send_verification_email(request, user, mail_subject, email_template)
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
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in!')
        return redirect('my_account')
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('my_account')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('signin_user')
    context = {}
    return render(request, 'accounts/signin_user.html', context)


def signout_user(request):
    auth.logout(request)
    messages.info(request, 'You are logged out')
    return redirect('signin_user')


@login_required(login_url='signin_user')
def my_account(request):
    user = request.user
    redirect_url = detect_user(user)
    return redirect(redirect_url)


@login_required(login_url='signin_user')
@user_passes_test(check_role_customer)
def customer_dashboard(request):
    return render(request, 'accounts/customer_dashboard.html')



