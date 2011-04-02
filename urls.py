from django.conf.urls.defaults import *
from django.contrib import admin
from . import settings
from tweetmatcher.views import *

admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^fetch/([A-Za-z0-9_-]{0,20})$', fetch), #send whatever's after the fetch delim as a username
	(r'^authors/$', authors),
	(r'^$', get_profile),
	
    # Example:
    # (r'^tweetmatcher/', include('tweetmatcher.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
   media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')
   urlpatterns += patterns('',
       (r'^%s/(?P<path>.*)$' % media_url, 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
   )