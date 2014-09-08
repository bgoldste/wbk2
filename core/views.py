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
import requests, re
import datetime
import calendar
import datetime
import pytz
from django.core.exceptions import MultipleObjectsReturned
import time
















class HomePageView(SuccessMessageMixin, CreateView):
    template_name = "index.html"
    form_class = EmailForm
    model = Subscriber
    success_url = '/#signup'
    success_message = "Thanks for being a part of Wavebook. We'll be in touch soon."
  
    def get_success_message(self, cleaned_data):
        return self.success_message 


def forecast(request, **kwargs):
	context = RequestContext(request)
	spot = kwargs.get("spot")
	try:
		spot = Spot.objects.get(name=spot) 	

		
		#context["HeaderTitles"] = getHeaderTitles(data)
		#context["ForecastData"] = getForecastData(data)
		context["all"] = getForecastData(spot)
		return render_to_response('wbk.html', context)


	except Spot.DoesNotExist:
		context["spot"] = "No spot with that name exists."
		return render_to_response('nospot.html', context)


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
	
		data = ForecastData.objects.filter(spot = spot.id ).order_by("date")

		context["images"] = ImageLink.objects.filter(ForecastData__spot=spot.id).order_by("-ForecastData__date")
		context["current_forecast"] = ForecastData.objects.filter(spot = spot.id ).order_by("-date")[0]

		#context["data"] = data
		
		return render_to_response('spot.html', context)
	except Spot.DoesNotExist:
		context["spot"] = "No spot with that name exists."
		return render_to_response('nospot.html', context)
	#except IndexError:
		#context["spot"] = "Index error returnign."
		#return render_to_response('nospot.html', context)

def spotList (request):
	context = RequestContext(request)
	context["spots"] = Spot.objects.all()
	return render_to_response("spotlist.html" , context)



def InstaScraperView(request, **kwargs):
	context = RequestContext(request)
	spot = kwargs.get("spot") 	
	context["spot"] = spot
	spot = Spot.objects.get(name=spot)
	

	base_url = "https://api.instagram.com/v1/media/search"
	max_timestamp = int(time.time())
	distance = 5000
	lat = spot.lat
	lon = spot.lon

	client_id="ad3fa66bd197402d98d490127e06d6d8"

	url = "%s?max_timestamp=%s&distance=%s&lat=%s&lng=%s&client_id=%s" % (base_url, max_timestamp, distance, lat, lon, client_id)

	data =requests.get(url).json()['data']
	images = ()
	dates = ()
	count = 0
	while len(images) < 40:
		count += 1
		#print "COUNT #" , count
		print "max time" , max_timestamp
		#print "len" , len(images)
		url = "%s?max_timestamp=%s&distance=%s&lat=%s&lng=%s&client_id=%s" % (base_url, max_timestamp, distance, lat, lon, client_id)

		data =requests.get(url).json()['data']

		


		for a in data:
			#print "max_timestamp", max_timestamp, "created_time for current ", a["created_time"]
			if max_timestamp > float(a["created_time"]):
				#print "changing time stamp"
				max_timestamp = a["created_time"]
			#print "max-time" , max_timestamp
			if a["caption"]:
			#print a["caption"]['text'].encode('utf-8')
		
			#print a["link"]
			#print '<img src="', str(a["images"]["standard_resolution"]['url']), '">'
		
				line = a["caption"]['text'].encode('utf-8')
				searchObj = re.search( r'(surf)+', line)
				if searchObj:
					#print a["caption"]['text'].encode('utf-8')
					#print a['link']
					#print "searchObj.group() : ", searchObj
					images += (a["images"]["standard_resolution"]['url'],)
					ImageLink.objects.get_or_create( url =a["images"]["standard_resolution"]['url'], ForecastData= matchdate(a, spot))
					
					#dates += (matchdate(a),)
				




		#grab forecast data associated w images
		#for a in images:
			#print a

	


	context["images"] = images
	context["dates"] = dates
	return  render_to_response("insc.html", context)




def matchdate(img, spot):
	print "MATCHDATE CREATED TIME PULL" , img["created_time"]
	img = int(img["created_time"])
	print  datetime.datetime.utcfromtimestamp(img)
	date = datetime.datetime.utcfromtimestamp(img).replace(tzinfo=pytz.UTC)


	lte = ForecastData.objects.filter(spot= spot, date__lte=date).order_by('-date')
	gte = ForecastData.objects.filter(spot = spot, date__gt=date).order_by('date')

	if lte or gte:
	   lte_obj =None
	   gte_obj = None
	   if not lte:
	    	return gte[0]
	   else:
	      lte_obj = lte[0]

	   if not gte:
	      return lte[0]
	   else:
	      gte_obj = gte[0]
	   import math
	   timestamp_diff = abs(lte_obj.date - date) > abs(gte_obj.date- date)

	   return  gte_obj if timestamp_diff else lte_obj
	return  None