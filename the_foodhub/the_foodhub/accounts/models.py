from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import models as auth_models, get_user_model
from the_foodhub.accounts.managers import FoodHubUserManager
from datetime import datetime
from django.utils import timezone


class FoodHubUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    MAX_FIRST_NAME_LENGTH = 50
    MAX_LAST_NAME_LENGTH = 50
    MAX_USERNAME_LENGTH = 50
    MAX_PHONE_NUMBER_LENGTH = 15
    RESTAURANT = 1
    CUSTOMER = 2

    ROLE_CHOICE = (
        (RESTAURANT, 'Restaurant'),
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

    is_staff = models.BooleanField(
        default=False,
    )

    is_active = models.BooleanField(
        default=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = FoodHubUserManager()

    def __str__(self):
        return self.email





