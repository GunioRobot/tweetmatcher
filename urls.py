from django.conf.urls.defaults import *
from . import settings
from tweetmatcher.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^fetch/([A-Za-z0-9_-]{0,20})$', fetch),
	(r'^authors/$', authors),
	(r'^$', get_profile),
    (r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
   media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')
   urlpatterns += patterns('',
       (r'^%s/(?P<path>.*)$' % media_url, 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
   )