from django.db import models


class Author(models.Model):
    username = models.CharField(max_length=30, unique=True)
    screen_name = models.CharField(max_length=100)
    profile_image_url = models.URLField()
    def __unicode__(self):
        return self.twitter_username


class Tweet(models.Model):
    twitter_id = models.BigIntegerField(unique=True)
    body = models.CharField(max_length=140)
    author = models.ForeignKey(Author)
    created_at = models.DateTimeField()
    def __unicode__(self):
        return self.body

        
class Hashtag(models.Model):
    text = models.CharField(max_length=139)
    author = models.ForeignKey(Author)
    def __unicode__(self):
        return self.text

        
class Mention(models.Model):
    name = models.CharField(max_length=139)
    author = models.ForeignKey(Author)
    def __unicode__(self):
        return self.name
