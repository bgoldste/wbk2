import json
import urllib
import datetime
from pytz import timezone
import pytz


#todo
#write funciton map urls to spots

#retrieve the results for the day before
current_forecasts_version =json.load(urllib.urlopen("https://www.kimonolabs.com/api/b113cv24?apikey=cda20781a4dc08939339ef86f55893a6&kimwithurl=1"))['version']
results = json.load(urllib.urlopen("https://www.kimonolabs.com/api/%d/b113cv24?apikey=cda20781a4dc08939339ef86f55893a6&kimwithurl=1" % (int(current_forecasts_version) - 1)))
print "forecasts received on " , results["thisversionrun"]

results2 = json.load(urllib.urlopen("https://www.kimonolabs.com/api/8qfvx0ts?apikey=cda20781a4dc08939339ef86f55893a6&kimwithurl=1"))
print "reports received on " , results2["thisversionrun"]
#results['results']['collection1'] is a list of all objects in collection1

#data in a list of all the data objects
all_forecasts = results['results']['collection1']
all_reports = results2['results']['collection1']


def get_today_forecast():
	"""returns a list of forecasts for todays date (theoretically these were generated the day before)"""
	today_forecast = []
	#if you iterate over data, you can a dict of each data object
	for  row in all_forecasts:
		#filter for only todays date...eeeek
		date = datetime.datetime.now(tz=pytz.utc)
		date = date.astimezone(timezone('US/Pacific'))
		if row["date"].find("%d/%d" % (date.month, date.day)) != -1:
			today_forecast.append(row)

			#print "Match", row["date"]
	return today_forecast


def get_today_report():
	"""returns a list of reports for todays date"""
	today_reports = []
	for row in all_reports:
		date = datetime.now(tz=pytz.utc)
		if row["date"].find("%s %d" % (datetime.date.today().strftime("%B"), datetime.date.today().day)) != -1:
			today_reports.append(row)
		return today_reports
	#print all_reports

def compare(report, forecast):
	"""compare forecast for a spot with most recent report"""
	print 'report', report['url']
	print 'forecast' , forecast['url']





def get_matches():

	spot_region_pairs = {
	'ocean-beach' :  'sf-san-mateo-county',
	'steamer-lane' : 'santa-cruz',

	'malibu' : 'north-los-angeles',
	'lower-trestles' :'south-orange-county',
	'c-street': 'ventura',
	}

	total_matches = 0
	matches = []
	for a in get_today_forecast():
		
		for b in all_reports:
		
			for k, v in spot_region_pairs.items():
			
				if a["url"].find(v) != -1 and b["url"].find(k) != -1:
					total_matches += 1

					forecast_rating =  a["rating"] 
					report_rating = b["conditions"]

					forecast_wvht = a["wvht"].replace("ft", " ")
					report_wvht =  b["wvht"].replace("ft", "")


					detail = (k, a["rating"],   forecast_wvht , b["conditions"] , report_wvht , report_rating == forecast_rating, report_wvht == forecast_wvht)   #spot, forecast, report 
					matches.append(detail)
			
	return matches
	



#print matches 














"""
for k, v in spot_region_pairs.items():
	for a in get_today_forecast():
		for b in get_today_report():
			
			#print k, a['url']
			#print v , b['url']
			
			if (a['url'].find(v) != -1 and b['url'].find(k) != -1):
				print "forecast and report matched for " , b["spot"]

				#print "Forecast from ",a["date"], ": ", a["rating"] , a["wvht"],   a["url"]
				#print "report from ", b["date"], b["conditions"], b["wvht"], b["report"], b["spot"]


"""


"""
results['results']  {u'collection1': [{u'rating': u'fair', u'wvht': u'3-4ft+', u'url': u'http://www.surfline.com/surf-forecasts/central-california/santa-cruz_2958/', u'spot': u'Santa Cruz', u'detail': u'Old SSW swell and WSW/NW swell mix fades', u'date': u'Saturday - 09/20'}, {u'rating': u'fair', u'wvht': u'2-3ft+', u'url': u'http://www.surfline.com/surf-forecasts/central-california/santa-cruz_2958/', u'spot': u'', u'detail': u"New, mid period NW swell fills in; larger sets to 3-5' at best NW exposed breaks north of town; small SSW leftovers", u'date': u'Sunday - 09/21'}, {u'rating': u'poor to fair', u'wvht': u'1-3ft', u'url': u'http://www.surfline.com/surf-forecasts/central-california/santa-cruz_2958/', u'spot': u'', u'detail': u'Dropping WNW swell; minor SSW swell leftovers', u'date': u'Monday - 09/22'}, {u'rating': u'poor to fair', u'wvht': u'2-4ft', u'url': u'http://www.surfline.com/surf-forecasts/central-california/sf-san-mateo-county_2957/', u'spot': u'SF-San Mateo County', u'detail': u'Old W/NW and SSW swell mix fades; new WNW swell due in late; light AM winds', u'date': u'Saturday - 09/20'}, {u'rating': u'fair', u'wvht': u'4-6ft', u'url': u'http://www.surfline.com/surf-forecasts/central-california/sf-san-mateo-county_2957/', u'spot': u'', u'detail': u'New WNW swell builds in and peaks; small SSW leftovers; light AM winds', u'date': u'Sunday - 09/21'}, {u'rating': u'fair', u'wvht': u'3-4ft+', u'url': u'http://www.surfline.com/surf-forecasts/central-california/sf-san-mateo-county_2957/', u'spot': u'', u'detail': u'Dropping WNW swell; minor SSW swell; light AM winds', u'date': u'Monday - 09/22'}, {u'rating': u'fair', u'wvht': u'2-3ft+', u'url': u'http://www.surfline.com/surf-forecasts/southern-california/south-orange-county_2950/', u'spot': u'South Orange County', u'detail': u'SW-SE swell mix drops at exposed spots; NW swell mix fades; Still some fun peaky shaped waves at top combo spots at times especially during the first half of the day', u'date': u'Saturday - 09/20'}, {u'rating': u'poor to fair', u'wvht': u'2-3ft', u'url': u'http://www.surfline.com/surf-forecasts/southern-california/south-orange-county_2950/', u'spot': u'', u'detail': u'SW-SE swell mix drops further at exposed spots; old NW swell-mix fades; Top combo magnets pull in larger waist-chest high sets on proper tides w/ fair conditions', u'date': u'Sunday - 09/21'}, {u'rating': u'poor to fair', u'wvht': u'2-3ft', u'url': u'http://www.surfline.com/surf-forecasts/southern-california/south-orange-county_2950/', u'spot': u'', u'detail': u'Small NW swell due, old SW swell drops; Minimal new SSW pulse joins in late', u'date': u'Monday - 09/22'}, {u'rating': u'fair', u'wvht': u'2-3ft+', u'url': u'http://www.surfline.com/surf-forecasts/southern-california/ventura_2952/', u'spot': u'Ventura', u'detail': u'SW-SE swell mix drops at exposed spots; fading NW swell-mix; biggest early', u'date': u'Saturday - 09/20'}, {u'rating': u'poor to fair', u'wvht': u'1-3ft', u'url': u'http://www.surfline.com/surf-forecasts/southern-california/ventura_2952/', u'spot': u'', u'detail': u'SW-SE swell mix drops further at exposed spots; NW swell-mix fades', u'date': u'Sunday - 09/21'}, {u'rating': u'poor to fair', u'wvht': u'1-3ft', u'url': u'http://www.surfline.com/surf-forecasts/southern-california/ventura_2952/', u'spot': u'', u'detail': u'Small NW swell due; old SW swell drops out; Minimal new SSW limps in late', u'date': u'Monday - 09/22'}, {u'rating': u'fair', u'wvht': u'2-3ft', u'url': u'http://www.surfline.com/surf-forecasts/southern-california/north-los-angeles_2142/', u'spot': u'North Los Angeles', u'detail': u'SW-SE swell mix drops at exposed spots; Small NW swell fades. Peaky for exposed beach breaks', u'date': u'Saturday - 09/20'}, {u'rating': u'poor to fair', u'wvht': u'1-3ft', u'url': u'http://www.surfline.com/surf-forecasts/southern-california/north-los-angeles_2142/', u'spot': u'', u'detail': u'SW-SE swell mix drops further at exposed spots; old NW swell-mix fades', u'date': u'Sunday - 09/21'}, {u'rating': u'poor to fair', u'wvht': u'1-2ft', u'url': u'http://www.surfline.com/surf-forecasts/southern-california/north-los-angeles_2142/', u'spot': u'', u'detail': u'Small NW swell due, old SW swell drops out; Minimal new SSW pulse joins in late', u'date': u'Monday - 09/22'}]}
rating=fair 
wvht=3-4ft+ 
url=http://www.surfline.com/surf-forecasts/central-california/santa-cruz_2958/ 
spot=Santa Cruz 
detail=Old SSW swell and WSW/NW swell mix fades 
date=Saturday - 09/20 
"""