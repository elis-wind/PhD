import requests
import time
#import urllib.request
from urllib import request
import webbrowser

with open('word_list.txt', 'r') as f:
    words = f.read().splitlines()

    
for word in words:
    segment = request.quote(word.encode('cp1251'))
      
    # Old version of Ruscorpora  
    #url1 = "https://search1.ruscorpora.ru/search.xml?env=alpha&mycorp=&mysent=&mysize=&mysentsize=&mydocsize=&spd=&text=lexgramm&mode=main&sort=gr_tagging&lang=ru&nodia=1&parent1=0&level1=0&lex1="+segment+"&gramm1=&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=&gramm2=&sem2=&sem-mod2=sem&sem-mod2=sem2&flags2=&m2=&p=0"

    # New version of Ruscorpora
    url1 = "https://processing.ruscorpora.ru/search.xml?env=alpha&api=1.0&mycorp=&mysent=&mysize=&mysentsize=&dpp=&spp=&spd=&ct=&mydocsize=&mode=main&lang=ru&sort=i_grtagging&nodia=1&text=lexgramm&parent1=0&level1=0&lex1="+word+"&gramm1=&sem1=&flags1=&sem-mod1=sem&sem-mod1=semx&morph1=&parent2=0&level2=0&min2=1&max2=1&lex2=&gramm2=&sem2=&flags2=&sem-mod2=sem&sem-mod2=semx&morph2="

    url2 = "https://www.google.com/search?channel=fs&client=ubuntu&q="+word

    webbrowser.open(url1, new=2)
    webbrowser.open(url2, new=2)

    time.sleep(2) #prevent "429 Too Many Requests" error