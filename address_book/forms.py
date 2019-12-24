from django import forms
from .models import addressModel
class addressForm(forms.ModelForm):
    class Meta:
        model = addressModel
        fields = ['Name','Email','Mobile','City']