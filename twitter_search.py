#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 15:22:54 2018

@author: apple
"""
import csv
import time
import glob
import pandas as pd


def twitter_search(category, keywords, numbers_of_tweets):
    
        client = get_twitter_client()
        n = numbers_of_tweets    
        temp = []
        influencer = []

        
        for k in keywords:
            count = 0
            results = client.search(q = k, lang = 'en')  
            for tweet in results:
                if tweet.user.screen_name not in influencer:
                    influencer.append(tweet.user.screen_name)
                    if 'RT @' not in tweet.text and tweet.retweet_count > 0 and count < n:
                        lines = [k, tweet.user.screen_name, str(tweet.created_at), tweet.favorite_count, tweet.retweet_count, tweet.text]
                        temp.append(lines)
                        count = count + 1
                else: 
                    break
                
            if count == 0:
                print(k + ' not found.')
            else:
                print(k + ' finished, '+str(count)+' of tweets found, go to next keyword')
        
        with open("Influencers_"+ category, 'w') as csv_file:
            writer = csv.writer(csv_file)
            fields = ['keywords', 'User', 'Time', 'Favorite count', 'retweets', 'Text']
            writer.writerow(fields)
            
            for lines in temp:
                writer.writerow(lines)
            
            #print(tweet.user.screen_name + " Tweeted at: "+str(tweet.created_at)+ " about "+ tweet.text+"\n")
            
def search_by_category(path):
    csvs = []
    
    for fname in glob.glob1(path, '*.csv'):
        csvs.append(fname)
    
    for category in csvs:
        dataset = pd.read_csv(category, encoding = "ISO-8859-1")
        x = dataset.iloc[:,0]
        keywords = []
        
        for keyword in x:
            keywords.append(keyword)
            
        print("Start Searching "+ category +" Influencers")    
        twitter_search(category, keywords, 100)
        print(category + " completed, rest for 1 min.")
        time.sleep(60)
              
path = "/Users/apple/__Twitter__/0605/projects"
search_by_category(path)



