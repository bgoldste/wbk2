import requests
from datetime import datetime
from pytz import timezone
import pytz
from django.utils import timezone
from core.models import ForecastData, Spot
from django.core.exceptions import MultipleObjectsReturned
import datetime
import calendar
from datetime import datetime
import pytz
from django.core.exceptions import MultipleObjectsReturned
import time
import requests, re
from core.models import *


def getAllData(Spot):
	#returns split list of all data. will have to hardcode in length of line for now. Later pass it in
	return(requests.get(Spot.url).text.split)
	
def getHeaderTitles(data):
	#returns header titles as list
	HeaderTitles = data[5:19]
	HeaderTitles.insert(0, "Date and Time")
	
	return(HeaderTitles)

def getForecastData(Spot):
	#reads data from the url attached to a spot, and save data to db w/ foreign key
	data = requests.get(Spot.url).text.split()
	print "data received"
	entries = 19
	HeaderTitles = entries * 2
	count = HeaderTitles

	ReturnData = []
	print "start iterating through data"
	while (len(data)!=count):
		current_row = data[count:(count + entries)]
		
		date = convertDate(current_row[0:5])
		remaining_data = current_row[5:]
		for index, item in enumerate(remaining_data):
			if item == 'MM':
				remaining_data[index] = None
				

		remaining_data.insert(0, date)
		ReturnData.append(remaining_data)
		try:
			print ForecastData.objects.get_or_create(
				date = date, spot = Spot,
				WDIR = remaining_data[1], WSPD = remaining_data[2], GST = remaining_data[3],
				WVHT = remaining_data[4], DPD = remaining_data[5], APD = remaining_data[6], 
				MWD = remaining_data[7], PRES = remaining_data[8], ATMP = remaining_data[9], 
				WTMP = remaining_data[10], DEWP = remaining_data[11], VIS = remaining_data[12], 
				PTDY = remaining_data[13], TIDE = remaining_data[14]
				)

			#print "entry added"
			count += entries

			
		except MultipleObjectsReturned:
			print "returning because multiple returned"
			return(ReturnData)

	return(ReturnData)

def convertDate(dataRow):
	#date = str(dataRow[0:5])
	#date = datetime.strptime(date, '%Y %m %d %H, %M')

	utc = timezone.utc
	date = map(int,dataRow)
	date = datetime(date[0],date[1],date[2],date[3],date[4],tzinfo=utc)
	return (date)




def getInstagram(spot):
	
	
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
	while len(images) < 150:
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
					

	return 

def matchdate(img, spot):
	print "MATCHDATE CREATED TIME PULL" , img["created_time"]
	img = int(img["created_time"])
	print  datetime.utcfromtimestamp(img)
	date = datetime.utcfromtimestamp(img).replace(tzinfo=pytz.UTC)


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