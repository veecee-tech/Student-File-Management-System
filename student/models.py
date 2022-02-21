from django.db import models
from authentication.models import Account
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_currentuser.middleware import get_current_authenticated_user
# Create your models here.


class StudentProfile(models.Model):
    
    
    gender_choice = (
        ("male", "Male"),
        ("Female", "Female"),
    )

    user = models.OneToOneField(to=Account, related_name="studentprofile", null=True, on_delete=models.CASCADE)
    adviser =models.ForeignKey(to=Account, related_name="adviser", null=True, on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    mat_no = models.CharField(max_length=14, null=True, blank=True)
    student_id = models.CharField(max_length=8, null=True, blank=True)
    gender = models.CharField(choices=gender_choice, max_length=10, null=True, blank=True)
    



@receiver(post_save, sender=Account)
def create_profile(sender, instance, created,**kwargs):
    # user = getattr(instance, 'current_authenticated_user')
    if created and instance.is_student:
        StudentProfile.objects.create(user=instance, adviser=get_current_authenticated_user())
    else:
        pass


# @receiver(post_save, sender=Account)
# def update_profile(sender, instance, created, **kwargs):

#     if created == False:
#         instance.profile.save()

class StudentDocuments(models.Model):

    user = models.OneToOneField(to=Account, related_name="studentdocument", on_delete=models.CASCADE)
    admission_letter = models.ImageField(upload_to='academic_records/')
    jamb_original_result = models.ImageField(upload_to='academic_records/')
    ssce_1 = models.ImageField(upload_to='academic_records/')
    ssce_2 = models.ImageField(upload_to='academic_records/')
    jamb_adm_letter = models.ImageField(upload_to='academic_records/')
    state_of_origin = models.ImageField(upload_to='academic_records/')
    birth_cert = models.ImageField(upload_to='academic_records/')
    course_reg_100 = models.ImageField(upload_to='academic_records/', blank=True, null=True)
    payment_slip_100 = models.ImageField(upload_to='academic_records/', blank=True, null=True)
    course_reg_200 = models.ImageField(upload_to='academic_records/', blank=True, null=True)
    payment_slip_200 = models.ImageField(upload_to='academic_records/', blank=True, null=True)
    course_reg_300 = models.ImageField(upload_to='academic_records/', blank=True, null=True)
    payment_slip_300 = models.ImageField(upload_to='academic_records/', blank=True, null=True)
    course_reg_400 = models.ImageField(upload_to='academic_records/', blank=True, null=True)
    payment_slip_400 = models.ImageField(upload_to='academic_records/', blank=True, null=True)
    course_reg_500 = models.ImageField(upload_to='academic_records/', blank=True, null=True)
    payment_slip_500 = models.ImageField(upload_to='academic_records/', blank=True, null=True)
    
    # def __str__(self):
    #     return user_username

@receiver(post_save, sender=Account)
def upload_file(sender, instance, created,**kwargs):
    
    if created and instance.is_student:
        StudentDocuments.objects.create(user=instance)
    else:
        pass