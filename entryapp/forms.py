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
        fields = ("labid_text", "name_text", "cash_amount", "cheque_amount", "eftpos_amount" ,"location", "staff_code")
        widgets = {
            'name_text': forms.TextInput(attrs={'class': 'form-control'}),
            "labid_text": forms.TextInput(attrs={'class': 'form-control'}),
            "cheque_amount": forms.TextInput(attrs={'class': 'form-control'}),
            "cash_amount": forms.TextInput(attrs={'class': 'form-control'}),
            "eftpos_amount": forms.TextInput(attrs={'class': 'form-control'}),
            "location": forms.Select(attrs={'class': 'form-control'}),
            "staff_code": forms.TextInput(attrs={'class': 'form-control'})
        }