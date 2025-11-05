from django import forms
from .models import Bin

class ReportBinForm(forms.ModelForm):
    class Meta:
        model = Bin
        fields = ['name','location','fill_percent','latitude','longitude']
        widgets = {
            'fill_percent': forms.NumberInput(attrs={'min':0,'max':100})
        }
