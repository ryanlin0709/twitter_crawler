#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Download user information


import os
import json
import pandas as pd
import time

from twython import Twython
from tweepy import Cursor
from twitter_client import get_twitter_client


#FOR OAUTH AUTHENTICATION -- NEEDED TO ACCESS THE TWITTER API
def user_search(user_list):
    client = get_twitter_client()
       
    #Load user IDs
    dataset = pd.read_csv(user_list, encoding = "ISO-8859-1")
    x = dataset.iloc[:,1]
    ids = []
    for id in x:
        ids.append(id)   
    #ACCESS THE LOOKUP_USER METHOD OF THE TWITTER API -- GRAB INFO ON UP TO 100 IDS WITH EACH API CALL
    #THE VARIABLE USERS IS A JSON FILE WITH DATA ON THE 32 TWITTER USERS LISTED 
    for x in range(0, len(ids), 100):
        chunks = ids[x:x+100]
        
        for user in chunks:
            profile = client.get_user(screen_name = user)
            users.append(profile._json)
            print(user)


def user_search2(user_list):
    t = Twython('nJFz1FISj32bOSS98mTZcL8FE', 'Kg1uKfrZAX7uEjwwmUX02RzWy8mM83bBMZJDmOtzdMk7721PxZ')
       
    #Load user IDs
    dataset = pd.read_csv(user_list, encoding = "ISO-8859-1")
    x = dataset.iloc[:,1]
    ids = []
    for id in x:
        ids.append(id)
     
    #ACCESS THE LOOKUP_USER METHOD OF THE TWITTER API -- GRAB INFO ON UP TO 100 IDS WITH EACH API CALL
    #THE VARIABLE USERS IS A JSON FILE WITH DATA ON THE 32 TWITTER USERS LISTED 
    users = []
    for user in ids:
        users.append(t.lookup_user(screen_name = user)[0])
        print(user)
    return users

def twitter_get_timeline(user_list, numbers_of_tweets, dir_name):    
    client = get_twitter_client()
    n = numbers_of_tweets
    
    dirname = "tweets/{}".format(dir_name)
    os.makedirs(dirname, mode=0o755, exist_ok=True)
    
    for x in range(0, len(user_list), 20):
        chunks = user_list[x:x+20]         
        for entry in chunks: 
            print(entry['screen_name'])
            fname = "{}/user_timeline_{}.jsonl".format(dirname, entry['screen_name'])
            with open(fname, 'w') as f:
                for tweet in Cursor(client.user_timeline, screen_name = entry['screen_name']).items(n):
                        f.write(json.dumps(tweet._json)+"\n")

def twitter_get_timeline2(user_list, numbers_of_tweets, dir_name):    
    client = get_twitter_client()
    n = numbers_of_tweets
    
    dirname = "tweets/{}".format(dir_name)
    os.makedirs(dirname, mode=0o755, exist_ok=True)
    
    for x in range(0, len(user_list), 20):
        chunks = user_list[x:x+20]         
        for entry in chunks: 
            fname = "{}/user_timeline_{}.jsonl".format(dirname, entry)
            with open(fname, 'w') as f:
                for tweet in Cursor(client.user_timeline, screen_name = entry).items(n):
                        f.write(json.dumps(tweet._json)+"\n")
            print(entry)

                      
#Batch
rest = []
for entry in influencers:
    rest.append(entry['screen_name'])
    
        
        

        





    


