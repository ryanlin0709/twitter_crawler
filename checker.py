#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 17:09:23 2018

@author: apple
"""
import os.path
import pandas as pd

dirname = 'All5'

user_list = 'Influencers_{}.csv'.format(dirname)
dataset = pd.read_csv(user_list, encoding = "ISO-8859-1")
x = dataset.iloc[:,1]
ids = []
for id in x:
    ids.append(id)


rest = []
i = 1

for entry in users:
    dir_name = dirname
    screen_name = entry['screen_name']
    tweet_file = 'tweets/{}/user_timeline_{}.jsonl'.format(dir_name, screen_name)
    
    if os.path.isfile(tweet_file):
        print(str(i))
        i += 1
    else:
        rest.append(screen_name)
        
for entry in rest:
    dir_name = dirname
    screen_name = entry
    tweet_file = 'tweets/{}/user_timeline_{}.jsonl'.format(dir_name, screen_name)
    
    if os.path.isfile(tweet_file):
        del rest[rest.index(entry)]

        
#檢查重複
one = []
two = []
for entry in user:
    if entry['screen_name'] not in one:
        one.append(entry['screen_name'])
    else:
        two.append(entry['screen_name'])
        
#Count Project
projects = []

cate = 'Technology'
plist = '{}.csv'.format(cate)
dataset = pd.read_csv(plist, encoding = "ISO-8859-1")
x = dataset.iloc[:,0]

for p in x:
    if p not in projects:
        projects.append(p)

#Score 
user_list = 'score.csv'
dataset = pd.read_csv(user_list, encoding = "ISO-8859-1")
x = dataset.iloc[:,0]
names = []
for name in x:
    names.append(name)

target = 'All5_influencer_information_over_1000.csv'
dataset = pd.read_csv(target, encoding = "ISO-8859-1")
x = dataset.iloc[:,0]
names2 = []
for name in x:
    names2.append(name)

no_score = []

for name in names2:
    if name not in names:
        print(name)
    
    


    
        
        
