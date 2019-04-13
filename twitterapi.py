# Import the necessary package to process data in JSON format
# -*- coding: utf-8 -*-
try:
    import json
except ImportError:
    import simplejson as json

# Import the tweepy library
import tweepy

# Variables that contains the user credentials to access Twitter API
ACCESS_TOKEN = 'DO NOT TOUCH'
ACCESS_SECRET = 'DO NOT TOUCH'
CONSUMER_KEY = 'DO NOT TOUCH'
CONSUMER_SECRET = 'DO NOT TOUCH'

# Setup tweepy to authenticate with Twitter credentials:

auth = tweepy.OAuthHandler("NORMAL ENTER HERE", "SECRET ENTER HERE")
auth.set_access_token("NORMAL ENTER HERE", "SECRET ENTER HERE")

# Create the api to connect to twitter with your creadentials
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
#---------------------------------------------------------------------------------------------------------------------
# wait_on_rate_limit= True;  will make the api to automatically wait for rate limits to replenish
# wait_on_rate_limit_notify= Ture;  will make the api  to print a notification when Tweepyis waiting for rate limits to replenish
#---------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------
# The following loop will print most recent statuses, including retweets, posted by the authenticating user and that user’s friends.
# This is the equivalent of timelinehome on the Web.
#---------------------------------------------------------------------------------------------------------------------

hasht = tweepy.Cursor(api.search, q='igotpizza').items(100)

for tweet in hasht:
    print(tweet.created_at, tweet.text, tweet.id)
    api.update_status("@" + tweet.user.name  + ' Enjoy your pizza' + "        You once tweeted         " + tweet.text, tweet.id)


#---------------------------------------------------------------------------------------------------------------------
# Twitter API development use pagination for Iterating through timelines, user lists, direct messages, etc.
# To help make pagination easier and Tweepy has the Cursor object.
#---------------------------------------------------------------------------------------------------------------------
