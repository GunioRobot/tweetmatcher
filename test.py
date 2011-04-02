import types
import re

def parse_tweets_test(file):
    #open file and read contents into resource
    f = open(file)
    f = f.read()
    #split the file on newlines
    posts = f.split('\n')
    # instantiate lists for hashtags and profiles
    h = []
    p = []
    #step through tweets and place 
    # hashtags and profiles into the lists
    for post in posts:
            get_hashtags(post)
            get_profiles(post)
    
    print h
    print p
    
    
def get_hashtags(post):
    """
    Searches for hashtags within a tweet
    
    returns List of hashtags
    """
    pattern = "(#.+)"
    
    hashtags = re.search(pattern, post)
    if hashtags is not None:
        print hashtags

def get_profiles(post):
    """Searches for user profiles within a tweet
    
    returns List of profiles"""
    pattern = "(@.{1,20})"
    
    p = re.search(pattern, post)
    if p is not None:
        print p


parse_tweets_test('tweets.txt')