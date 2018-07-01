# Chap02-03/twitter_client.py

import twython as Twython
from tweepy import API
from tweepy import OAuthHandler

def get_twitter_auth():
    
    consumer_key = 'YBlJtJhYPp1FhHUrrhQiHBV6D'
    consumer_secret = 'JmeHq1c9PyLDmWRHAWonjACC2JqLzzPg8hPMtja9qtu0sv5g0G'
    access_token = '956055299777056770-CkBnHqyiWNnNeLv7B3k7JGaCTyIlACI'
    access_secret = 'x5Qmopw9fcrkpfjFxgFFanVQEhWdx1cxkoQVlwMYkIwY4'
  
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    
    return auth

def get_twitter_auth2():
    
    consumer_key = 'nJFz1FISj32bOSS98mTZcL8FE'
    consumer_secret = 'Kg1uKfrZAX7uEjwwmUX02RzWy8mM83bBMZJDmOtzdMk7721PxZ'
    access_token = '956055299777056770-lSpILa4oPowGQp62rkrpul1gjHZXA4s'
    access_secret = 'W3X27iGjAFy9J8MDGMDcsWXnZfh8e13cZ477Z63wAA0ws'
  
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    
    return auth

def get_twitter_client():
    """Setup Twitter API client.

    Return: tweepy.API object
    """
    auth = get_twitter_auth2()
    client = API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)
    return client

def get_twython_auth():
    
    twython = Twython('YBlJtJhYPp1FhHUrrhQiHBV6D','JmeHq1c9PyLDmWRHAWonjACC2JqLzzPg8hPMtja9qtu0sv5g0G')
    return twython