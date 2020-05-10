from django import forms

class PaymentForm(forms.Form):
    name_text = forms.CharField(max_length=200)
    labid_text = forms.CharField(max_length=9)
    amount_text = forms.CharField(max_length=200)
    type_text = forms.CharField(max_length=200)
    location_text = forms.CharField(max_length=200)