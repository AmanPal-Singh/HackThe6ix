from django.forms import ModelForm
from risk.models import Address

class crowdsourceForm(ModelForm):

	class Meta:
		model = Address
		fields = ['address', 'insurance_value']


