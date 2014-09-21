from django.core.management.base import BaseCommand, CommandError
from core.models import ForecastData, Spot
from wbk2.tasks import *

class Command(BaseCommand):
    args = '<Spot Name >'
    help = 'bens Command'

    def handle(self, *args, **options):

    	for a in Spot.objects.all():
            print "getting forecast data for %s" % a 
    	    getForecastData(a)
            print "forecast data received, getting instagram for  %s" % a 
            getInstagram(a)

        	
           
            #spot = Spot.objects.get(pk=int(spot_id))
        
            #raise CommandError('Spot"%s " does not exist' % spot_name)

                
           