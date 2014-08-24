from django.db import models
import os
# Create your models here.
class Subscriber(models.Model):
	email_address = models.EmailField(unique=True)

	def __unicode__(self):
		return u'%s' % (self.email_address)

class Spot(models.Model):
	name = models.TextField(default="San Francisco", unique = True)
	url = models.TextField(default = 'http://ndbc.noaa.gov/data/5day2/42012_5day.txt', unique = True)

	def __unicode__(self):
		return u'%s' % (self.name)


class ForecastData(models.Model):
	
	date = models.DateTimeField()
	WDIR = models.FloatField(null=True)
	WSPD = models.FloatField(null=True)
	GST = models.FloatField(null=True)
	WVHT = models.FloatField(null=True)
	DPD = models.FloatField(null=True)
	APD = models.FloatField(null=True)
	MWD = models.FloatField(null=True)
	PRES = models.FloatField(null=True)
	ATMP = models.FloatField(null=True)
	WTMP = models.FloatField(null=True)
	DEWP = models.FloatField(null=True)
	VIS = models.FloatField(null=True)
	PTDY = models.FloatField(null=True)
	TIDE = models.FloatField(null=True)
	spot = models.ForeignKey(Spot, null = False, default=1)
	class Meta:
		unique_together = ("spot", "date")


	def __unicode__(self):
		return u'%s' % (self.date)



class ImageData(models.Model):
    data = models.ForeignKey(ForecastData, default=1)
    spot = models.ForeignKey(Spot, default =1)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    def __unicode__(self):
	
		return  u'%s' % (self.image)

 

	