from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.utils.text import slugify

from the_foodhub.accounts.forms import FoodHubUserCreationForm
from the_foodhub.accounts.models import FoodHubUser, Profile
from the_foodhub.accounts.utils import send_verification_email, check_role_vendor
from the_foodhub.vendor.forms import FoodHubVendorCreationForm
from django.contrib import messages


def signup_vendor(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in!')
        return redirect('my_account')
    elif request.method == 'POST':
        form = FoodHubUserCreationForm(request.POST)
        v_form = FoodHubVendorCreationForm(request.POST, request.FILES)
        if form.is_valid() and v_form.is_valid:
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = FoodHubUser.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                                   email=email, password=password)
            user.role = FoodHubUser.VENDOR
            user.save()
            vendor = v_form.save(commit=False)
            vendor.user = user
            vendor_name = v_form.cleaned_data['vendor_name']
            vendor.vendor_slug = slugify(vendor_name) + '-' + str(user.id)
            user_profile = Profile.objects.get(user=user)
            vendor.user_profile = user_profile
            vendor.save()

            # Send verification email
            mail_subject = 'Please activate your account'
            email_template = 'accounts/emails/account_verification_email.html'
            send_verification_email(request, user, mail_subject, email_template)

            messages.success(request, 'Your account has been registered successfully! Please wait for the approval.')
            return redirect('signup_vendor')
        else:
            print('invalid form')
            print(form.errors)
    else:
        form = FoodHubUserCreationForm()
        v_form = FoodHubVendorCreationForm()

    context = {
        'form': form,
        'v_form': v_form,
    }

    return render(request, 'vendor/signup_vendor.html', context)


@login_required(login_url='signin_user')
@user_passes_test(check_role_vendor)
def vendor_dashboard(request):
    return render(request, 'vendor/vendor_dashboard.html')


def vendor_profile(request):
    return render(request, 'vendor/vendor_profile.html')
