from django import forms
from .models import AdviserProfile

class UpdateAdviserProfileForm(forms.ModelForm):
    class Meta:
        model = AdviserProfile
        exclude = ['user']
        fields = "__all__"
