from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import models as auth_models
from the_foodhub.accounts.managers import FoodHubUserManager
from django.utils import timezone


class FoodHubUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    MAX_FIRST_NAME_LENGTH = 50
    MAX_LAST_NAME_LENGTH = 50
    MAX_USERNAME_LENGTH = 50
    MAX_PHONE_NUMBER_LENGTH = 15

    VENDOR = 1
    CUSTOMER = 2

    ROLE_CHOICE = (
        (VENDOR, 'Vendor'),
        (CUSTOMER, 'Customer'),
    )

    first_name = models.CharField(
        _('first name'),
        max_length=MAX_FIRST_NAME_LENGTH,
    )

    last_name = models.CharField(
        _('last name'),
        max_length=MAX_LAST_NAME_LENGTH,
    )

    username = models.CharField(
        _('username'),
        max_length=MAX_USERNAME_LENGTH,
        unique=True,
    )

    email = models.EmailField(
        _("email address"),
        unique=True,
        error_messages={
            "unique": _("A user with that email already exists."),
        },
    )

    phone_number = models.CharField(
        max_length=MAX_PHONE_NUMBER_LENGTH,
        blank=True,
        null=True
    )

    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICE,
        blank=True,
        null=True,
    )

    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    last_login = models.DateTimeField(_("last login"), default=timezone.now)
    created_date = models.DateTimeField("date created", default=timezone.now)
    modified_date = models.DateTimeField('date modified', default=timezone.now)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = FoodHubUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def get_role(self):
        if self.role == 1:
            user_role = 'Vendor'
        elif self.role == 2:
            user_role = 'Customer'
        return user_role


class Profile(models.Model):
    MAX_ADDRESS_LENGTH = 50
    MAX_COUNTRY_LENGTH = 20
    MAX_STATE_LENGTH = 20
    MAX_REGION_LENGTH = 20
    MAX_CITY_LENGTH = 20
    MAX_PIN_CODE_LENGTH = 6
    MAX_LONGITUDE_LENGTH = 20
    MAX_LATITUDE_LENGTH = 20

    profile_picture = models.ImageField(
        upload_to='users/profile_pictures/',
        blank=True,
        null=True
    )

    cover_photo = models.ImageField(
        upload_to='users/cover_photos/',
        blank=True,
        null=True
    )

    address_line_1 = models.CharField(
        max_length=MAX_ADDRESS_LENGTH,
        blank=True,
        null=True
    )

    address_line_2 = models.CharField(
        max_length=MAX_ADDRESS_LENGTH,
        blank=True,
        null=True
    )

    country = models.CharField(
        max_length=MAX_COUNTRY_LENGTH,
        blank=True,
        null=True
    )

    region = models.CharField(
        max_length=MAX_REGION_LENGTH,
        blank=True,
        null=True
    )

    city = models.CharField(
        max_length=MAX_CITY_LENGTH,
        blank=True,
        null=True
    )

    pin_code = models.CharField(
        max_length=MAX_PIN_CODE_LENGTH,
        blank=True,
        null=True
    )

    latitude = models.CharField(
        max_length=MAX_LATITUDE_LENGTH,
        blank=True,
        null=True
    )

    longitude = models.CharField(
        max_length=MAX_LONGITUDE_LENGTH,
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    modified_at = models.DateTimeField(
        auto_now_add=True
    )

    user = models.OneToOneField(
        FoodHubUser,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def full_address(self):
        return f'{self.address_line_1}, {self.address_line_2}'

    def __str__(self):
        return self.user.email
