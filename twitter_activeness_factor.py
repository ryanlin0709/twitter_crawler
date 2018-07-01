#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 21 14:42:13 2018

@author: apple
"""
search = 'All2'
dirname = 'All2'

influencers = user_search('Influencers_{}.csv'.format(search))
influencers = user_search2('Influencers_{}.csv'.format(search))
twitter_get_timeline(influencers, 1000, dirname)
twitter_get_timeline2(rest, 1000, dirname)

def life_long(date_time):
    month = time.strptime(date_time[4:7], "%b").tm_mon
    date = time.strptime(date_time[8:10], "%d").tm_mday
    year = time.strptime(date_time[-4:], "%Y").tm_year
    
    today =datetime.date.today()
    created_day = datetime.date(year, month, date)
    return (today - created_day).days


import time
import datetime
for entry in influencers:
    dir_name = dirname
    screen_name = entry['screen_name']
    first_day = entry['created_at']
    life = life_long(first_day)
    tweet_file = 'tweets/{}/user_timeline_{}.jsonl'.format(dir_name, screen_name)
    retweets = 0
    print(screen_name)
    

    with open(tweet_file) as f:
        for line in f:
            tweet = json.loads(line)
            if 'RT @' in tweet['text']:
                retweets += 1
    
    entry['life_long'] = life
    entry['Avg_tweets_per_day'] = round(entry['statuses_count']/life, 4)
    entry['Avg_favorite_per_day'] = round(entry['favourites_count']/life, 4)
    entry['Avg_retweets_per_day'] = round(retweets/life, 4)
    
