from django.contrib import admin
from tweetmatcher.tm.models import *

admin.site.register(Author)
admin.site.register(Hashtag)
admin.site.register(Tweet)