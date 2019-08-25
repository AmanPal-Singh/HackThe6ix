from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from risk.models import Address
from risk.forms import crowdsourceForm, insuranceForm
from django.forms import modelformset_factory

# Create your views here.

data = 0

def index(request):
	""" View function for home page of site """
	form = insuranceForm(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			data = request.POST.copy()
			address = request.POST.get('address')
			insurance_value = request.POST.get('insurance_value')
			print(address)
			print(insurance_value)
			
			return render(request, 'assessment.html', {'data': data, 'form': form, 'address': address, 'insurance_value': insurance_value})
	else:
		form = insuranceForm()

	return render(request, 'assessment.html', {'form': form})

def about(request):
	""" View function for about page """
	return render(request, 'about.html')

