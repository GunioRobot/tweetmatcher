from django import forms
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, Http404
from tm.models import *
from django.template.context import RequestContext

import twitter
import re

hash_regex = re.compile(r'#[0-9a-zA-Z+_]*',re.IGNORECASE) 
user_regex = re.compile(r'@[0-9a-zA-Z+_]*',re.IGNORECASE)

def fetch(request, username):
	"""uses the string sent after the trailing slash from 
	fetch as a username to get the latest 20 tweets from username
	"""
	client = twitter.Api()
	latest_posts = client.GetUserTimeline(username)
	tweets = [s.text for s in latest_posts]
	
	# check to see if the username is already in the database and if not, create a new author
	try: 
		author = Author.objects.get(twitter_username=username)
	except Author.DoesNotExist:	
		# if username.is_valid?
		# currently any old username is saved regardless of validity
		author = Author(twitter_username=username)
		author.save()
	
	# set up empty lists for hashtag and mentions
	user_mentions = []
	hashtags = []
	
	for t in tweets:
		for tt in user_regex.finditer(t):
			if tt.group(0) not in user_mentions:
				user_mentions.append(tt.group(0))		
		for th in hash_regex.finditer(t):
			if th.group(0) not in hashtags:
				hashtags.append(th.group(0))	
	
	# check to see if the hashtags and mentions are already registered with the author
	# and if not, add them to the author's hashtags and mentions lists
	[author.hashtag_set.create(text=h) for h in hashtags if h not in author.hashtag_set.all()]
	[author.mention_set.create(name=u) for u in user_mentions if u not in author.mention_set.all()]
	[author.tweet_set.create(body=t) for t in tweets if t not in author.tweet_set.all()]
	
	return render_to_response('main.html',locals())
	

def authors(request):
	"""uses the string sent after the trailing slash from 
	fetch as a username to get the latest 20 tweets from username
	"""
	authors = Author.objects.all()
	return render_to_response('authors.html',context_instance=RequestContext(request,
	                                                                 locals()))
	
def get_profile(request):
	"""grabs a user's twitter profile and gives them back a list of hashtags, and keywords"""
	if request.method == "POST":
		form = GetProfileForm(request.POST)
		if form.is_valid(): # All validation rules pass
		            # Process the data in form.cleaned_data
		            # ...
		            return HttpResponseRedirect('fetch/%s' % form.profile) # Redirect after POST
	else:
		form = GetProfileForm()
		context = {'get_profile_form': form}
		return render_to_response('get_profile.html', context)
	
class GetProfileForm(forms.Form):
	profile = forms.CharField()	
	
	
def check_tw_name(name):
	"""Checks Twitter API for a legit username. Throws a friendly error if not found"""
	try:
		client = twitter.Api()
		user = client.GetUserTimeline(name)
	except Twitter.TwitterError:
		pass

