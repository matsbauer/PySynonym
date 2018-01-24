#!/usr/bin/env python3.4
# encoding: utf-8
# creator: matsbauer
# date created: 24.01.2018

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


#class PySynonym(object):
    
def find(word):
    req = Request('http://www.thesaurus.com/browse/%s'%word, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    status = BeautifulSoup(webpage, "html5lib").findAll("div", {"class": "relevancy-list"})[0] #Find the HTML class that contains the synonyms
    
    synonyms = [] #init return list for synonyms
    
    for tag in status.ul.findAll('li'):
        synonyms.append(tag.select('span.text')[0].get_text())
    return synonyms
    
if __name__ == "__main__":
    d = find('fun')
    print(d)
    