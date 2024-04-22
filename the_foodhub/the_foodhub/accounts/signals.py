from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import FoodHubUser, Profile


@receiver(post_save, sender=FoodHubUser)
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    print(created)
    if created:
        Profile.objects.create(user=instance)
    else:
        try:
            profile = Profile.objects.get(user=instance)
            profile.save()
        except:
            # Create the userprofile if not exist
            Profile.objects.create(user=instance)


@receiver(pre_save, sender=FoodHubUser)
def pre_save_profile_receiver(sender, instance, **kwargs):
    pass
# post_save.connect(post_save_create_profile_receiver, sender=FoodHubUser)
