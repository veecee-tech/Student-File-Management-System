from django.db import models
from authentication.models import Account
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class AdviserProfile(models.Model):

    MR, MRS, MS, DR, PROF ='Mr', 'Mrs', 'Ms', 'Dr', 'Prof'
    
    HONORFIC_TITLE = (
        (MR, 'Mr'),
        (MRS, 'Mrs'),
        (MS, 'Ms'),
        (DR, 'Dr'),
        (PROF, 'Prof'),
    )

    gender_choice = (
        ("male", "Male"),
        ("Female", "Female"),
    )

    user = models.OneToOneField(
        Account,
        verbose_name="Account",
        on_delete=models.CASCADE,
        related_name='adviserprofile', null=False)
    honorofic_title = models.CharField(
        max_length=4,
        choices=HONORFIC_TITLE,
        blank=True, null=True)
    first_name = models.CharField(blank=True, null=True, max_length=255)
    last_name = models.CharField(blank=True, null=True, max_length=255)
    email = models.EmailField(max_length=254, blank=True, null=True)
    gender = models.CharField(choices=gender_choice, max_length=10)


@receiver(post_save, sender=Account)
def create_profile(sender, instance, created, **kwargs):

    if created and instance.is_adviser:
        AdviserProfile.objects.create(user=instance)
    else:
        pass


# @receiver(post_save, sender=Account)
# def update_profile(sender, instance, created, **kwargs):

#     if created == False:
#         instance.adviserprofile.save()
    
  