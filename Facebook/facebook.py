#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 15:11:32 2021

@author: abhi
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import  datetime
from datetime import timedelta
import pandas as pd
import time
import json
from selenium.webdriver.common.keys import Keys
import re

searchUser=['Himadri sarmah']
users=[     'abhinava.goswami.35']
Output_MM=[]
path1=['https://m.facebook.com/iamSagardeepTalukdar/posts/3320023114720980','https://m.facebook.com/himantabiswasarma/posts/10158560131803983']
i=0
t=1
A=1
for path in path1:
    postText =[]
    comments=[]
    browser = webdriver.Firefox(executable_path='/opt/WebDriver/bin/geckodriver')
    browser.get(path)
    soup1=BeautifulSoup(browser.page_source,"html.parser")
    pt=soup1.find("div",{"class":"_5rgt _5nk5"}).text
    postText.append(pt)
    try:
        loadMore=browser.find_element_by_class_name("_108_")
        
        while loadMore == True:
            
            loadMore.click()
    except:
        print("no more to load")
    pt1=soup1.findAll("div",{"class":"_2b06"})
    for i in pt1:
        comments.append(i.text)
