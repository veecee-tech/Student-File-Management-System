from django import forms
from .models import StudentProfile,StudentDocuments
from django_currentuser.middleware import get_current_authenticated_user

from authentication.models import Account

class CreateStudent(forms.ModelForm):
    class Meta:
        model = StudentProfile
        exclude = ('user','adviser',)
        fields = "__all__"

class UpdateStudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        exclude = ['user','adviser']
        fields = "__all__"


class UploadDocumentForm100(forms.ModelForm):
    class Meta:
        model = StudentDocuments
        exclude = [
                'user', 'course_reg_200', 'payment_slip_200',
                'course_reg_300', 'payment_slip_300','course_reg_400', 'payment_slip_400',
                'course_reg_500', 'payment_slip_500'
                ]
       
        fields = '__all__'
   
class UploadDocumentForm200(forms.ModelForm):
    class Meta:
        model = StudentDocuments
        exclude = [
                'user', 'course_reg_100', 'payment_slip_100',
                'course_reg_300', 'payment_slip_300','course_reg_400', 'payment_slip_400',
                'course_reg_500', 'payment_slip_500'
                ]
        fields = '__all__'
    
class UploadDocumentForm300(forms.ModelForm):
    class Meta:
        model = StudentDocuments
        exclude = [
                'user', 'course_reg_200', 'payment_slip_200',
                'course_reg_100', 'payment_slip_100','course_reg_400', 'payment_slip_400',
                'course_reg_500', 'payment_slip_500'
                ]
        fields = '__all__'

class UploadDocumentForm400(forms.ModelForm):
    class Meta:
        model = StudentDocuments
        exclude = [
                'user', 'course_reg_200', 'payment_slip_200',
                'course_reg_300', 'payment_slip_300','course_reg_100', 'payment_slip_100',
                'course_reg_500', 'payment_slip_500'
                ]
        fields = '__all__'
   
class UploadDocumentForm500(forms.ModelForm):
    class Meta:
        model = StudentDocuments
        exclude = [
                'user', 'course_reg_200', 'payment_slip_200',
                'course_reg_300', 'payment_slip_300','course_reg_400', 'payment_slip_400',
                'course_reg_100', 'payment_slip_100'
                ]
        fields = '__all__'
    
