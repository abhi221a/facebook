#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 15:11:32 2021

@author: abhi
"""

from selenium import webdriver

from bs4 import BeautifulSoup

import pandas as pd

import json


searchUser=['Himadri sarmah']
users=[     'abhinava.goswami.35']
Output=[]
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
    Output.append("Post Text")
    Output.appent(postText)
    try:
        loadMore=browser.find_element_by_class_name("_108_")
        
        while loadMore == True:
            
            loadMore.click()
    except:
        print("no more to load")
    pt1=soup1.findAll("div",{"class":"_2b06"})
    for i in pt1:
        comments.append(i.text)
    
    Output.append("Comments")
    Output.appent(comments)
    A+=1
    
df=pd.DataFrame(Output)
with open("/home/abhi/Desktop/"+A, "w") as json_file:
        json.dump(Output, json_file)
browser.quit()