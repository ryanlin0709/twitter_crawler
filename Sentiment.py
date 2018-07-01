#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  4 12:59:10 2018

@author: apple
"""
import nltk
import csv
import numpy as np
import pandas as pd
import glob

negative = []
with open("words-negative.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        negative.append(row)
        
positive = []
with open("words-positive.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        positive.append(row)

def sentiment(text):
    temp = []
    text_sent = nltk.sent_tokenize(text)
    for sentence in text_sent:
        n_count = 0
        p_count = 0
        sent_words = nltk.word_tokenize(sentence)
        for word in sent_words:
            for item in positive:
                if word == item[0]:
                    p_count += 1
            for item in negative:
                if word == item[0]:
                    n_count +=1
        if p_count > 0 and n_count == 0:
            temp.append(1)
        elif n_count%2 > 0:
            temp.append(-1)
        elif n_count%2 == 0 and n_count > 0:
            temp.append(1)
        else:
            temp.append(0)
    return temp

def sentiment_analysis(file_name):
    dataset = pd.read_csv(file_name)
    x = dataset.iloc[:,3]
    tweets = []
    Sentiment = []
    
    for tweet in x:
        tweets.append(tweet)
        
    for tweet in tweets:
        Sentiment.append(np.average(sentiment(str(tweet))))
        
    dataset['Sentiment'] = Sentiment
    dataset.to_csv(file_name, index = False)
    

path = "/Users/apple/__Twitter__/0503/User/"
csvs = []
for fname in glob.glob1(path, '*.csv'):
    csvs.append(fname)
    
for f in csvs:
    sentiment_analysis(f)
    


