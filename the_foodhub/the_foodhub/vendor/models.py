from django.db import models

from the_foodhub.accounts.models import FoodHubUser, Profile
from the_foodhub.accounts.utils import send_notification

class Vendor(models.Model):
    MAX_VENDOR_NAME_LENGTH = 50

    user = models.OneToOneField(
        FoodHubUser,
        related_name='user',
        on_delete=models.CASCADE,
    )

    user_profile = models.OneToOneField(
        Profile,
        related_name='userprofile',
        on_delete=models.CASCADE,
    )

    vendor_name = models.CharField(
        max_length=MAX_VENDOR_NAME_LENGTH,
    )

    vendor_license = models.ImageField(
        upload_to='vendor/licence',
    )

    is_approved = models.BooleanField(
        default=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    modified_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.vendor_name

    def save(self, *args, **kwargs):
        if self.pk is not None:
            orig = Vendor.objects.get(pk=self.pk)
            if orig.is_approved != self.is_approved:
                mail_template = 'accounts/emails/vendor_approved_email.html'
                context = {
                    'user': self.user,
                    'is_approved': self.is_approved,
                }
                if self.is_approved:
                    mail_subject = 'Congratulations! Your restaurant has been approved'
                    send_notification(mail_subject, mail_template, context)
                else:
                    mail_subject = 'Your restaurant has not been approved on our marketplace'

                    send_notification(mail_subject, mail_template, context)

        return super(Vendor, self).save(*args, **kwargs)
