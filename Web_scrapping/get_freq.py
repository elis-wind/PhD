mport requests
#import urllib.request
from urllib import request
import time
from bs4 import BeautifulSoup, NavigableString, Tag
from re import split
import regex as re

with open('corpora.txt', 'r') as f:
    corpora = f.read().splitlines()

with open('word_list.txt', 'r') as f:
    words = f.read().splitlines()

for corpus in corpora:
    #req_segment = request.quote(segment.encode('cp1251'))
    print(corpus)
    
    for word in words:
        #out_file = open(segment+"_"+corpus+".txt","a+")
        segment = request.quote(word.encode('cp1251'))
        
        url1 = "https://search1.ruscorpora.ru/search.xml?env=alpha&mycorp=&mysent=&mysize=&mysentsize=&mydocsize=&spd=&text=lexgramm&mode="+corpus+"&sort=gr_tagging&lang=ru&nodia=1&parent1=0&level1=0&lex1="+segment+"&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=&gramm2=&sem2=&sem-mod2=sem&sem-mod2=sem2&flags2=&m2=&p=0"
        #print(url1)
        
        #get number of pages for each word
        try:
            response1 = requests.get(url1)
            soup1 = BeautifulSoup(response1.text, "html.parser")
            stats = soup1.find_all("span", {"class": "stat-number"})
            entries = stats[4].text
            entries = re.sub(" ", "", entries)
            entries = re.sub("[^0-9]", "", entries)
            #pages = (int(entries) // 50) + 1
            print(word, "\t", entries)
        except:
            print(word, "\t", "0")
            continue