from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from risk.models import Address
from risk.forms import crowdsourceForm
from django.forms import modelformset_factory

# Create your views here.



data = 0

def index(request):
	""" View function for home page of site """
	crowdSourceForm = modelformset_factory(Address, fields=('address', 'insurance_value'))
	
	if request.method == 'POST':
		formset = crowdSourceForm(request.POST, request.FILES)
		if formset.is_valid():
			print(formset)
			formset.save()
			data = request.POST.copy()
			print(data)
			return render(request, 'assessment.html', {'data': data})
	else:
		formset = crowdSourceForm()

	data = request.POST.copy()

	return render(request, 'index.html', {'formset': formset})