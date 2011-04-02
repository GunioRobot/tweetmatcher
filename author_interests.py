# import settings
# from tm.models import *
import re
from counter import *
# 
# andy = Author.objects.get(twitter_username="the_pied_pipes")
# 
# tweets = andy.tweet_set.all()
# 

word_boundary = re.compile(r'\b',re.IGNORECASE)

f = open("tweets.txt")
tweets = []
while f.readline() != "":
	tweets.append(f.readline())

words = Counter([])

for t in tweets:
	tweet_words = t.split()
	words.update(tweet_words)
	
print words

# for t in tweets:
# 	tweet_words = t.split()
# 	for tw in tweet_words:
# 		if tw not in words:
# 			count = 1
# 			words.extend = [word=tw, count=count]
# 			words.append(tw)
# 		else:
# 			[v=count+1 for k,v in words if k=tw]
# 			print words
