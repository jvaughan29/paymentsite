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
        fields = ("name_text", "labid_text", "amount_text", "type_text", "location_text")