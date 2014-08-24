# Create your views here.

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import CreateView
from forms import EmailForm, SpotForm
from django import forms
from core.models import *
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
	getForecastData(Spot.objects.all()[0])
	#context["HeaderTitles"] = getHeaderTitles(data)
	#context["ForecastData"] = getForecastData(data)
	context["all"] = ForecastData.objects.all().values_list().order_by("-date")

	return render_to_response('wbk.html', context)


class AddSpotView(SuccessMessageMixin, CreateView):
    template_name = "addspot.html"
    form_class = SpotForm
    model = Spot
    success_url = '/admin'
    #success_message = "Thanks for being a part of Wavebook. We'll be in touch soon."
  
    def get_success_message(self, cleaned_data):
        return self.success_message 



def SpotView(request, **kwargs):
	context = RequestContext(request)
	spot = kwargs.get("spot") 	

	try:
		spot = Spot.objects.get(name=spot)
		context["spot"] = (spot)
		image_set2 = []
		image_set = ImageData.objects.filter(spot=spot.id).order_by("-data")
		context["images"] = image_set[0].image.url
		for a in image_set:
			
			image_set2.append(a) 
		context["imageset2"] = image_set2

		context["data"] = ForecastData.objects.all().values_list().order_by("-date")
		context["total_objects"] = len(ForecastData.objects.all())
		return render_to_response('spot.html', context)
	except Spot.DoesNotExist:
		context["spot"] = "Got Nada por you bro."
		return render_to_response('nospot.html', context)
	except IndexError:
		context["spot"] = "Got Nada por you bro."
		return render_to_response('nospot.html', context)