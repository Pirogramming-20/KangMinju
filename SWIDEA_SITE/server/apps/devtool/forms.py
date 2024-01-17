from django import forms
from .models import DevTool

class DevForm(forms.ModelForm):
    class Meta():
        model = DevTool
        fields = ('__all__')