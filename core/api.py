from tastypie.resources import ModelResource
from core.models import Spot, ImageLink, ForecastData
from tastypie import fields
from tastypie.constants import ALL, ALL_WITH_RELATIONS

class SpotResource(ModelResource):
	#forecastdatas = fields.ToManyField('core.api.ForecastDataResource', 'forecastdatas',full=True)
	class Meta:
	    queryset = Spot.objects.all()
	    resource_name = 'spot'




class ForecastDataResource(ModelResource):
	spot = fields.ToOneField(SpotResource, 'spot')
	
	class Meta:
	    queryset = ForecastData.objects.all()
	    resource_name = 'forecastdata'
	    filtering = {
         
            "spot" : ALL_WITH_RELATIONS,
            "WDIR" : ['gte', 'lte'],
        

        }



class ImageLinkResource(ModelResource):
	ForecastData = fields.ForeignKey(ForecastDataResource, 'ForecastData' , full=True)

	class Meta:
	    queryset = ImageLink.objects.all()
	    resource_name = 'imagelink'
	    filtering = {
           
            "ForecastData": ALL_WITH_RELATIONS,
            "Spot" : ALL_WITH_RELATIONS,	
        }
