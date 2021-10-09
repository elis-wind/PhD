import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from re import split

file = open("ный_general","a+")

for g in range(0, 1153):
    url = "http://search2.ruscorpora.ru/search.xml?sort=gr_tagging&out=normal&dpp=100&spd=100&seed=31879&env=alpha&mycorp=&mysent=&mysize=&mysentsize=&mydocsize=&text=lexgramm&mode=main&lang=ru&nodia=1&parent1=0&level1=0&lex1=*%ED%FB%E9&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=&gramm2=&sem2=&sem-mod2=sem&sem-mod2=sem2&flags2=&m2=&p="+str(g)
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
    
