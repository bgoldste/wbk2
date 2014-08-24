from django.conf.urls import patterns, include, url
from django.contrib import admin
from core.views import HomePageView,forecast, AddSpotView, SpotView
import core
import settings


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
 	url(r'^wbk/', core.views.forecast,),
 	url(r'^addspot/', AddSpotView.as_view()),
 	url(r'^spots/(?P<spot>[\w]{0,10})$', SpotView),

)
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))