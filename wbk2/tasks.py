import requests
from datetime import datetime
from pytz import timezone
import pytz
from django.utils import timezone
from core.models import ForecastData, Spot

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

	while (len(data)!=count):
		current_row = data[count:(count + entries)]
		
		date = convertDate(current_row[0:5])
		remaining_data = current_row[5:]
		for index, item in enumerate(remaining_data):
			if item == 'MM':
				remaining_data[index] = None
				

		remaining_data.insert(0, date)
		ReturnData.append(remaining_data)

		ForecastData(
			date = date, spot = Spot,
			WDIR = remaining_data[1], WSPD = remaining_data[2], GST = remaining_data[3],
			WVHT = remaining_data[4], DPD = remaining_data[5], APD = remaining_data[6], 
			MWD = remaining_data[7], PRES = remaining_data[8], ATMP = remaining_data[9], 
			WTMP = remaining_data[10], DEWP = remaining_data[11], VIS = remaining_data[12], 
			PTDY = remaining_data[13], TIDE = remaining_data[14]
			).save()

		print "entry added"
		count += entries

	return(ReturnData)

def convertDate(dataRow):
	#date = str(dataRow[0:5])
	#date = datetime.strptime(date, '%Y %m %d %H, %M')

	utc = timezone.utc
	date = map(int,dataRow)
	date = datetime(date[0],date[1],date[2],date[3],date[4],tzinfo=utc)
	return (date)
