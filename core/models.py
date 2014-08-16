from django.db import models

# Create your models here.
class Subscriber(models.Model):
	email_address = models.EmailField()

	def __unicode__(self):
		return u'%s' % (self.email_address)

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
	def __unicode__(self):
		return u'%s' % (self.date)