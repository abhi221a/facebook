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

path1=['https://m.facebook.com/iamSagardeepTalukdar/posts/3320023114720980','https://m.facebook.com/himantabiswasarma/posts/10158560131803983']
i=0
t=1
t1=1
A=1

for path in path1:
    Output=[]
    postText =[]
    comments=[]
    browser = webdriver.Firefox(executable_path='/opt/WebDriver/bin/geckodriver')
    browser.get(path)
    soup1=BeautifulSoup(browser.page_source,"html.parser")
    pt=soup1.find("div",{"class":"_5rgt _5nk5"}).text
    postText.append(pt)
    Output.append("Post Text")
    Output.append(postText)
    try:
        loadMore=browser.find_element_by_class_name("_108_")
        
        while loadMore == True:
            t+=1
            loadMore.click()
    except:
        print("no more to load")
    soup1=BeautifulSoup(browser.page_source,"html.parser")
    pt1=soup1.findAll("div",{"class":"_2b06"})
    try:
        morereply=browser.find_element_by_class_name("_4ayk")
        
        while morereply == True:
            t1+=1
            morereply.click()
        soup1=BeautifulSoup(browser.page_source,"html.parser")
        try:
            reply=soup1.findAll("div",{"class":"_2b1k"}) 
        except:
            print("")
    except:
        print("no replies")
    
    
    z1=0 
    for i in pt1:
        comments.append(i.text)
        try:
             z=reply[z1]
        except:
             print('')
             if z1>=(len(reply)-1):
                 break
        reply1=z.findAll("div",{"class":"_2b04"})
        for j in reply1:
            nested=[]
            Output.append(j.text)
            
            
            if z1>=(len(reply)-1):
                break
    
    Output.append("Comments")
    Output.append(comments)
    
    df=pd.DataFrame(Output)
    with open("/home/abhi/Desktop/"+str(A), "w") as json_file:
        json.dump(Output, json_file)
    browser.quit()
    A+=1
