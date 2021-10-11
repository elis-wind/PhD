import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from re import split

file = open("ный_general","a+")

for g in range(0, 1037):
    url = "https://search1.ruscorpora.ru/search.xml?sort=gr_tagging&out=normal&dpp=100&spd=100&seed=12794&env=alpha&mycorp=&mysent=&mysize=&mysentsize=&mydocsize=&text=lexform&mode=main&lang=ru&nodia=1&req=*%ED%FB%E9&p="+str(g)
    try:
        response = requests.get(url)
        #print(url, response)
        soup = BeautifulSoup(response.text, "html.parser")
        #print(soup.prettify())
        ol = soup.find("ol")
        exemple = ol.text
        #print(exemple)
        file.write(exemple)
        print(g)
    except:
        continue
    
