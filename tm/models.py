from django.db import models

class Author(models.Model):
    twitter_username = models.CharField(max_length=30)
    email = models.EmailField()
    def __unicode__(self):
        return self.twitter_username

class Tag(models.Model):
    body = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    def __unicode__(self):
        return self.body

class Tweet(models.Model):
    body = models.CharField(max_length=140)
    author = models.ForeignKey(Author)
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