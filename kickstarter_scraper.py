#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 12 13:16:24 2018

@author: apple
"""


from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import csv
import re
import time



def scroll_down(id):
    option = webdriver.ChromeOptions()
    option.add_argument("--incognito")
    browser = webdriver.Chrome(executable_path='/users/apple/chromedriver', chrome_options=option)
    browser.get('https://www.kickstarter.com/discover/advanced?state=live&category_id=' + id +'&sort=popularity')
    
    while True:
        try:
            loadMoreButton = browser.find_element_by_xpath("//a[@class='bttn bttn-green bttn-medium']")
            time.sleep(2)
            loadMoreButton.click()
            time.sleep(5)
        except:
            print(id + 'Complete')
            break
    return browser

def get_element(browser):
    
    project_element = browser.find_elements_by_xpath("//a[@class='soft-black hover-text-underline']")
    projects = []
    for x in project_element:
        if len(x.text) > 1:
            name = x.text.split(' -')[0]
            name = name.split(':')[0]
            name = name.split(' | ')[0]
            name = name.split('\"')[0]
            projects.append(name)
    
    project_owner = browser.find_elements_by_xpath("//a[@class='soft-black hover-text-underline medium']")
    owners = []
    for x in project_owner:
        if len(x.text) > 1:
            owners.append(x.text)
            
    project_funded = browser.find_elements_by_xpath("//div[@class='type-13 mr2 dark-grey-500 medium']")
    funded = []
    for x in project_funded:
        if len(x.text) > 1:
            number = x.text.rstrip(' funded')
            funded.append(number)
    
    return projects, owners, funded

def write_to_csv(elements ,name):
    with open( name + '.csv', 'w') as csv_file:
        fields = "Project Owner Funded".split()
        writer = csv.writer(csv_file)
        writer.writerow(fields)
        
        projects = elements[0]
        owners = elements[1]
        funded = elements[2]
        
        for project, owner, fund in zip(projects, owners, funded):
            lines = [project, owner, fund]
            writer.writerow(lines)
            
            

ids = { "Technology":'16', "Publishing":'18', "Game":'12', "Art":'1', "Desgin":'7'}
for keys in ids:
    browser = scroll_down(ids[keys])
    test = get_element(browser)
    write_to_csv(test, str(keys))
    




    


