from django.contrib import admin
from core.models import Subscriber, ForecastData, Spot, ImageData

admin.site.register(Subscriber)
admin.site.register(ForecastData)
admin.site.register(Spot)
admin.site.register(ImageData)