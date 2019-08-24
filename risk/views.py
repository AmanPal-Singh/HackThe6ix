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
	#crowdSourceForm = modelformset_factory(Address, fields=('address', 'insurance_value'))
	form = insuranceForm(request.POST)
	if request.method == 'POST':
		#formset = crowdSourceForm(request.POST, request.FILES)
		if form.is_valid():
			data = request.POST.copy()
			print(data)
			return render(request, 'assessment.html', {'data': data})
	else:
		form = insuranceForm()
		#formset = crowdSourceForm()

	return render(request, 'index.html', {'form': form})