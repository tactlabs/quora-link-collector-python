#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on May 10, 2018

Course work: 

@author: 

Source:
'''


import requests
import re
from bs4 import BeautifulSoup

def main(research_later):
    
    for question in research_later:
        
        #print(question)
        #x = question
        #x[:-17]
        #print(x)
        #question[: -17]
        #print(question)

        goog_search = "https://www.google.com/search?source=hp&ei=FfLzWsxUjOC-BJHuu_gG&q=" + question
    
    
        r = requests.get(goog_search)
    
        soup = BeautifulSoup(r.text, "html.parser")
        print (soup.find('cite').text)
    
research_later = [
    "delete column from pandas dataframe using del df column name + quora",
    "why are python lambdas useful + quora",
    "if python is interpreted what are pyc files + quora"
        ]

    

if __name__ == '__main__':
    main(research_later)