import requests

def getAllData():
	#returns split list of all data. will have to hardcode in length of line for now. Later pass it in
	return(requests.get('http://ndbc.noaa.gov/data/5day2/42012_5day.txt').text.split())
	
def getHeaderTitles(data):
	#returns header titles as list
	HeaderTitles = data[0:19]
	
	return(HeaderTitles)

def getForecastData(data):
	#returns just the data (baby)

	#skip past 1st two rows. Change from hardcoding later.
	entries = 19
	HeaderTitles = entries * 2
	count = HeaderTitles

	ForecastData = []
	print "type ForecastData=", type(ForecastData)
	print "type data[count:(count+entries)]", type(data[count:(count+entries)])
	while (len(data)!=count):
		ForecastData.append(data[count:(count+entries)])
		count += entries
	print ForecastData
	print count, "?=", len(data)
	print ForecastData
	return(ForecastData)
