#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 14:03:39 2018

@author: apple
"""

from selenium import webdriver 
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('All2_influencer_information_over_1000.csv')
X = dataset.iloc[:,0].values
ids = []
for name in X:
    ids.append(name)

def search_score(id):
    option = webdriver.ChromeOptions()
    option.add_argument("--incognito")
    browser = webdriver.Chrome(executable_path='/users/apple/chromedriver', chrome_options=option)
    browser.get('https://moz.com/followerwonk/bio/?q=' + id +'&q_type=all&frmin=0&frmax=0&flmin=0&flmax=0&stctmin=0&stctmax=0')
    
    score = []
    project_element = browser.find_elements_by_xpath("//div/table/tbody/tr/td/div[@class='sa_score']")
    
    for x in project_element:
        score.append(x.text)
    browser.close()
    return score[0]

scores = {}
for i in ids:
    print(i)
    scores[i] = search_score(i)
    
    

