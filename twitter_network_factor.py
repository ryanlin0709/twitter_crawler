#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 21 11:21:29 2018

@author: apple
"""
import csv
import json
from twitter_client import get_twitter_client
from twitter_user_information import user_search

search = 'Technology'
dirname = 'Technology'

influencers = user_search('Influencers_{}.csv'.format(search))

    


"""
with open('Network_factor.csv', 'w') as csv_file:
        fields = "screen_name followers_count friends_count mutual_friends users_reached_by_1-degree_connections \
        avg_followers_for_followers listed_number".split()
        writer = csv.writer(csv_file)
        writer.writerow(fields)
        
        for entry in influencers:
            info = (entry['screen_name'], entry['followers_count'], entry['friends_count'], entry['mutual_friends'], entry['users reached by 1-degree connections'], entry['avg_followers for followers'], entry['listed_count'])
            writer.writerow(info)
"""


