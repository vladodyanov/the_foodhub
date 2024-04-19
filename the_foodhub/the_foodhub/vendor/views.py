from django.shortcuts import render, redirect
from the_foodhub.accounts.forms import FoodHubUserCreationForm
from the_foodhub.accounts.models import FoodHubUser, Profile
from the_foodhub.vendor.forms import FoodHubVendorCreationForm
from django.contrib import messages


def signup_vendor(request):
    if request.method == 'POST':
        form = FoodHubUserCreationForm(request.post)
        vendor_form = FoodHubVendorCreationForm(request.POST, request.FILES)
        if form.is_valid() and vendor_form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            user = FoodHubUser.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password1=password1
            )
            user.role = FoodHubUser.VENDOR
            user.save()
            vendor = vendor_form.save(commit=False)
            vendor.user = user
            user_profile = Profile.objects.get(user=user)
            vendor.user_profile = user_profile
            vendor.save()
            messages.success(request, 'Your account as vendor has been registered successfully! '
                                      'Please wait for approval and confirmation.')
            return redirect('signup_vendor')
        else:
            print('invalid form')
            print(form.errors)
    else:
        form = FoodHubUserCreationForm()
        vendor_form = FoodHubVendorCreationForm()

    content = {
        'form': form,
        'vendor_form': vendor_form,
    }

    return render(request, 'vendor/signup_vendor.html', content)
