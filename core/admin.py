from django.contrib import admin
from core.models import Subscriber, ForecastData, Spot

admin.site.register(Subscriber)
admin.site.register(ForecastData)
admin.site.register(Spot)