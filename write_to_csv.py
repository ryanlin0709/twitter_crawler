#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 15:43:07 2018

@author: apple
"""

import csv

with open('{}_influencer_information.csv'.format(search), 'w') as csv_file:
        fields = "screen_name life_long Number_of_statues Length_of_description \
        followers_count friends_count listed_number \
        Avg_tweets_per_day  Avg_favorite_per_day Avg_retweets_per_day\
        Most_favorited Avg_favorited_per_tweet Avg_favorites_per_user \
        Most_retweeted Avg_retweeted_per_tweet Avg_retweets_per_user \
        Avg_length_of_tweets sentiment_score Avg_hashtags_per_tweet tweets_with_hashtags \
        tweets_with_media tweets_with_url retweet_rate\
        influence_score".split()
        writer = csv.writer(csv_file)
        writer.writerow(fields)
        
        for entry in influencers:
            info = (entry['screen_name'], entry['life_long'], entry['statuses_count'],  entry['Length_of_description'], 
                    entry['followers_count'], entry['friends_count'], entry['listed_count'],
                    entry['Avg_tweets_per_day'], entry['Avg_favorite_per_day'], entry['Avg_retweets_per_day'],
                    entry['Most_favorited'], entry['Avg_favorited'], entry['Avg_favorites_per_user'], 
                    entry['Most_retweeted'], entry['Avg_retweeted'], entry['Avg_retweets_per_user'],
                    entry['Avg_length_of_tweets'], entry['sentiment_score'], entry['Avg_hashtags_per_tweet'], entry['tweets_with_hashtags'],
                    entry['tweets_with_media'], entry['tweets_with_url'], entry['retweet_rate'],
                    entry['influence_score'])
            writer.writerow(info)