# Create your views here.

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import CreateView
from forms import EmailForm
from django import forms
from core.models import Subscriber
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from wbk2.tasks import getForecastData, getHeaderTitles, getAllData

class HomePageView(SuccessMessageMixin, CreateView):
    template_name = "index.html"
    form_class = EmailForm
    model = Subscriber
    success_url = '/#signup'
    success_message = "Thanks for being a part of Wavebook. We'll be in touch soon."
  
    def get_success_message(self, cleaned_data):
        return self.success_message 


def forecast(request):
	context = RequestContext(request)
	data = getAllData()
	context["HeaderTitles"] = getHeaderTitles(data)
	context["ForecastData"] = getForecastData(data)
	return render_to_response('wbk.html', context)
