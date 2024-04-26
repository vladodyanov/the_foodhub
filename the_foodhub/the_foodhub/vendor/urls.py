from django.urls import path

from the_foodhub.accounts.views import vendor_dashboard
from the_foodhub.vendor.views import signup_vendor, vendor_profile

urlpatterns = (
    path('', vendor_dashboard, name='vendor'),
    path('signup_vendor/', signup_vendor, name='signup_vendor'),
    path('vendor_profile/', vendor_profile, name='vendor_profile'),
)