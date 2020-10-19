from django import forms
from django.forms import ModelForm
from .models import PaymentEntry

#class PaymentForm(forms.Form):
#   name_text = forms.CharField(max_length=200)
#   labid_text = forms.CharField(max_length=9)
#   amount_text = forms.CharField(max_length=200)
#   type_text = forms.CharField(max_length=200)
#   location_text = forms.CharField(max_length=200)

class PaymentForm(ModelForm):
    class Meta:
        model = PaymentEntry
        fields = ("name_text", "labid_text", "amount_double", "type", "location")
        widgets = {
            'name_text': forms.TextInput(attrs={'class': 'form-control'}),
            "labid_text": forms.TextInput(attrs={'class': 'form-control'}),
            "amount_double": forms.TextInput(attrs={'class': 'form-control'}),
            "type": forms.Select(attrs={'class': 'form-control'}),
            "location": forms.Select(attrs={'class': 'form-control'})
        }