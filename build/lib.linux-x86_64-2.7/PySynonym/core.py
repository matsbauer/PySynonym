#!/usr/bin/env python3.4
# encoding: utf-8
# creator: matsbauer
# date created: 24.01.2018

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

        
def synonym(word):
    req = Request('https://www.thesaurus.com/browse/%s'%word, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    status = BeautifulSoup(webpage, "html5lib").findAll("div", {"class": "relevancy-list"})[0] #Find the HTML class that contains the synonyms
    
    synonyms = [] #init return list for synonyms
    
    for tag in status.ul.findAll('li'):
        synonyms.append(tag.select('span.text')[0].get_text())
    
    return synonyms
    
    
def explain(word):
    req = Request('https://www.dictionary.com/browse/%s'%word, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    status = BeautifulSoup(webpage, "html5lib").findAll("div", {"class": "def-content"})[0] #Find the HTML class that contains the synonyms
    
    string = status.get_text().lstrip().rstrip()
    definition = " ".join(string.split())
    
    return definition
    
    
if __name__ == "__main__":
    d = explain('house')
    print(d)