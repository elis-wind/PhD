import requests
#import urllib.request
from urllib import request
import time
from bs4 import BeautifulSoup
from re import split
import regex as re

in_file = open('nn_list.txt', 'r')
lines = in_file.readlines()
in_file.close()

#read every word in txt file
for line in lines:
    line = line.strip()
    #encode word for url
    req = request.quote(line.encode('cp1251'))
    out_file = open(line+".txt","a+")

    url = "https://search1.ruscorpora.ru/search.xml?sort=gr_tagging&out=normal&dpp=100&spd=100&seed=10276&env=alpha&mycorp=&mysent=&mysize=&mysentsize=&mydocsize=&text=lexform&mode=main&lang=ru&nodia=1&req="+req+"&p=0"

    #get number of pages for each word
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        stats = soup.find_all("span", {"class": "stat-number"})

        entries = stats[3].text
        entries = entries.replace(" ", "")
        if len(entries) <= 2:
            pages = entries
        else: 
            pages = entries[:-2]
        print("number of pages for", line, "equals", pages)
    except:
        print("no entries found for", line)
        continue

    #get examples from each page for each word
    for g in range(0, int(pages)):
        url = "https://search1.ruscorpora.ru/search.xml?sort=gr_tagging&out=normal&dpp=100&spd=100&seed=10276&env=alpha&mycorp=&mysent=&mysize=&mysentsize=&mydocsize=&text=lexform&mode=main&lang=ru&nodia=1&req="+req+"&p="+str(g)
        try:
            response = requests.get(url)
            #print(url, response)
            soup = BeautifulSoup(response.text, "html.parser")
            #print(soup.prettify())
            ol = soup.find("ol")
            exemple = ol.text
            #print(exemple)
            out_file.write(exemple)
            print(g)
        except:
            continue
    
