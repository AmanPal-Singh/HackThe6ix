from django.forms import ModelForm
from django import forms
from risk.models import Address

class crowdsourceForm(ModelForm):

	class Meta:
		model = Address
		fields = ['address', 'insurance_value']


class insuranceForm(forms.Form):

	address = forms.CharField(label='Your address', max_length=200)
	insurance_value = forms.IntegerField(label='Your insurance')