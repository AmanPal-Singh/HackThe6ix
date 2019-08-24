from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Address(models.Model):
	""" This is the form question where an user can input an address """
	address = models.CharField(max_length = 200, help_text="Please enter the address of the property you would like assessment")

	def clean_address(self):
		""" This validates and returns cleaned data """
		data = self.cleaned_data['address']

		return data

	def __str__(self):
		"""String for representing the Model object."""
		return self.name

	""" This is the form question where an user can input their montly insurance """
	insurance_value = models.CharField(max_length = 200, help_text="Please enter your monthly insurance value")

	def clean_property_value(self):
		""" This validates and returns cleaned data """

		data = self.cleaned_data['insurance_value']

		# If the value is negative, raise an error
		if data < 0:
			raise ValidationError(_('Invalid insurance value - Value should be above $0.00'))
		return data

	def __str__(self):
		"""String for representing the Model object."""
		return self.name