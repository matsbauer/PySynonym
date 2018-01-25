#!/usr/bin/env python3.4
# encoding: utf-8
# creator: matsbauer
# date created: 24.01.2018

import sys
from bs4 import BeautifulSoup

if sys.version_info >= (3, 0):
    from urllib.request import Request, urlopen
else:
    from urllib2 import Request, urlopen
    

def synonym(word):
    req = Request('https://www.thesaurus.com/browse/%s'%word, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    status = BeautifulSoup(webpage, "html5lib").findAll("div", {"class": "relevancy-list"})[0] #Find the HTML class that contains the synonyms
    
    synonyms = [word] #adds the init word to the list
    
    if sys.version_info >= (3, 0): #if Python 2.x is used, the result has to be encoded.
        for tag in status.ul.findAll('li'):
            synonyms.append(tag.select('span.text')[0].get_text())
    else:
        for tag in status.ul.findAll('li'):
            synonyms.append(tag.select('span.text')[0].get_text().encode("utf-8"))
    
    return synonyms
    

def acronym(word):
    req = Request('https://www.thesaurus.com/browse/%s'%word, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    status = BeautifulSoup(webpage, "html5lib").findAll("div", {"class": "list-holder"})[0] #Find the HTML class that contains the synonyms
    
    acronyms = [] #init of return list
    
    if sys.version_info >= (3, 0): #if Python 2.x is used, the result has to be encoded.
        for tag in status.ul.findAll('li'):
            acronyms.append(tag.select('span.text')[0].get_text())
    else:
        for tag in status.ul.findAll('li'):
            acronyms.append(tag.select('span.text')[0].get_text().encode("utf-8"))
    
    return acronyms
    

def wordoftheday():
    req = Request('http://translate.reference.com/', headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    status = BeautifulSoup(webpage, "html5lib").findAll("a", {"class": "word"})[0] #Find the HTML class that contains the synonyms
    
    return status.get_text().capitalize()
    

def explain(word):
    req = Request('https://www.dictionary.com/browse/%s'%word, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    status = BeautifulSoup(webpage, "html5lib").findAll("div", {"class": "def-content"})[0] #Find the HTML class that contains the used definition
    
    string = status.get_text().lstrip().rstrip()
    definition = " ".join(string.split())
    
    return definition.capitalize()
   

def help():
    print("Get a list of synonyms using: ps.synonym('word')\n" + \
            "Get a word definition using: ps.explain('word')\n")
    

if __name__ == "__main__":
    testcase = acronym('fun')
    print(testcase)
    testcase = wordoftheday()
    print(testcase)
    testcase = explain('house')
    print(testcase)