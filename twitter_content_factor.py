#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 21 15:17:44 2018

@author: apple
"""
#Count user information
for entry in influencers:
    dir_name = dirname
    screen_name = entry['screen_name']
    tweet_file = 'tweets/{}/user_timeline_{}.jsonl'.format(dir_name, screen_name)
    favorites, retweets, replies, retweet_num, status_count = [], [], [], 0, 0
    print(screen_name)
    
    with open(tweet_file) as f:
        for line in f:
            status_count = status_count + 1 
            tweet = json.loads(line)
            favorites.append(tweet['favorite_count'])
            retweets.append(tweet['retweet_count'])
            if tweet['retweet_count'] > 0:
                retweet_num += 1
#retweet rate        
    if status_count > 0:
        retweet_rate = round(retweet_num/status_count, 4)
    else:
        retweet_rate = 0
    entry['retweet_rate'] = retweet_rate
        
#Favorite  
    entry['Most_favorited'] = sorted(favorites, reverse = True)[0]

    
    if status_count > 0:
        entry['Avg_favorited'] = round(sum(favorites)/status_count, 4) 
    else:
        entry['Avg_favorited'] = 0
 
    if entry['followers_count'] > 0:
        entry['Avg_favorites_per_user'] = round(sum(favorites)/ entry['followers_count'], 4)
    else:
        entry['Avg_favorites_per_user'] = 0

#Retweet   
    if len(retweets) > 0:
        entry['Most_retweeted'] = sorted(retweets, reverse = True)[0]
    else:
        entry['Most_retweeted'] = 0

    if status_count > 0:
        entry['Avg_retweeted'] = round(sum(retweets)/status_count, 4)
    else:
        entry['Avg_retweeted'] = 0
   
    if entry['followers_count'] > 0:
        entry['Avg_retweets_per_user'] = round(sum(retweets)/ entry['followers_count'], 4)
    else:
        entry['Avg_retweets_per_user'] = 0

#Count retweet score
for entry in influencers:
    dir_name = dirname
    screen_name = entry['screen_name']
    tweet_file = 'tweets/{}/user_timeline_{}.jsonl'.format(dir_name, screen_name)
    retweet_score ,status_count = [], 0
    print(screen_name)
    
    with open(tweet_file) as f:
        for line in f:
            status_count += 1
            tweet = json.loads(line)
            rt = tweet['retweet_count']
            retweet_score.append(rt * entry['retweet_rate'])
    entry['influence_score'] = round(sum(retweet_score)/ status_count, 4)    

#Analyse Content
for entry in influencers:
    dir_name = dirname
    screen_name = entry['screen_name']
    description = entry['description']
    tweet_file = 'tweets/{}/user_timeline_{}.jsonl'.format(dir_name, screen_name)
    total_characters = 0
    status_count = 0
    print(screen_name)
    
    with open(tweet_file) as f:    
        for line in f:
            tweet = json.loads(line)
            status_count = status_count + 1 
            text = tweet['text']
            total_characters += len(text)
            #tweet['character_count'] = len(text)
    entry['Avg_length_of_tweets'] = round(total_characters/ status_count, 4)
    entry['Length_of_description'] = len(description)

#Count Hashtags, media, urls
from collections import defaultdict
for entry in influencers:
    dir_name = dirname
    screen_name = entry['screen_name']
    description = entry['description']
    tweet_file = 'tweets/{}/user_timeline_{}.jsonl'.format(dir_name, screen_name)
    status_count, tweets_with_media, tweets_with_urls= 0, 0, 0
    print(screen_name)
    
    with open(tweet_file) as f:
        hashtag_count = defaultdict(int)
        hashtag_total = 0
        for line in f:
             status_count = status_count + 1
             tweet = json.loads(line)
             entities = tweet.get('entities', {})
             hashtags = entities.get('hashtags', [])
             hashtags_in_tweet = [tag['text'].lower() for tag in hashtags]
             n_of_hashtags = len(hashtags_in_tweet)
             hashtag_total += n_of_hashtags
             hashtag_count[n_of_hashtags] += 1
             
             media = entities.get('media', [])
             if media:
                 tweets_with_media += 1 
                 
             urls = entities.get('urls', [])
             if urls:
                 tweets_with_urls += 1 
        
        tweets_with_hashtags = sum([count for n_of_tags, count in hashtag_count.items() if n_of_tags > 0])
        
        tweets_no_hashtags = hashtag_count[0]
        tweets_with_hashtags_percent = "%.2f" % (tweets_with_hashtags / status_count)
        tweets_no_hashtags_percent = "%.2f" % (tweets_no_hashtags / status_count)
        tweets_with_media_percent = "%.2f" % (tweets_with_media/ status_count)
        tweets_with_url_percent = "%.2f" % (tweets_with_urls/ status_count)
    if tweets_with_hashtags > 0:
        entry['Avg_hashtags_per_tweet'] = round(hashtag_total/ tweets_with_hashtags, 4)
    else:
        entry['Avg_hashtags_per_tweet'] = 0
    entry['tweets_with_hashtags'] = tweets_with_hashtags_percent
    entry['tweets_without_hashtags'] = tweets_no_hashtags_percent
    entry['tweets_with_media'] = tweets_with_media_percent
    entry['tweets_with_url'] = tweets_with_url_percent
    
#Sentiment analysis
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer as analyser
ana = analyser()

for entry in influencers:
    dir_name = dirname
    screen_name = entry['screen_name']
    description = entry['description']
    tweet_file = 'tweets/{}/user_timeline_{}.jsonl'.format(dir_name, screen_name)
    score_total = 0
    status_count = 0
    print(screen_name)
    
    with open(tweet_file) as f:
        for line in f:
            results = []
            status_count = status_count + 1 
            tweet = json.loads(line)
            text = tweet['text']
            pol_score = ana.polarity_scores(text)
            compound = round(pol_score['compound'] * 100, 4)
            #tweet['compound'] = round(pol_score['compound'] * 100, 2)
            score_total += compound
    entry['sentiment_score'] = round(score_total/ status_count, 4)
    
             

    

