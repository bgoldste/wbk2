from django.conf.urls import patterns, include, url
from django.contrib import admin
from core.views import *
import core
import settings
from core.api import SpotResource, ImageLinkResource, ForecastDataResource

spot_resource = SpotResource()
image_link_resource = ImageLinkResource()
forecast_data_resource = ForecastDataResource()
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wbk2.views.home', name='home'),
    # url(r'^wbk2/', include('wbk2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
 	#url(r'^', HomePageView.as_view()),
 	url(r'^$', HomePageView.as_view()),
 	url(r'^wbk/(?P<spot>[\w]{0,10})$', core.views.forecast,),
 	url(r'^addspot/', AddSpotView.as_view()),
    url(r'^spots/$', spotList),
    url(r'^surfaudit/$', surfAudit),
 	url(r'^spots/(?P<spot>[\w]{0,10})$', SpotView),
    url(r'^insc/(?P<spot>[\w]{0,10})$', InstaScraperView),
    (r'^api/', include(spot_resource.urls)),
     (r'^api/', include(image_link_resource.urls)),

     (r'^api/', include(forecast_data_resource.urls)),



)
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))