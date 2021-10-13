import requests
#import urllib.request
from urllib import request
import time
from bs4 import BeautifulSoup, NavigableString, Tag
from re import split
import regex as re

with open('corpora.txt', 'r') as f:
    corpora = f.read().splitlines()

with open('segments.txt', 'r') as f:
    segments = f.read().splitlines()

#extract lemmas for every segment from every corpus
for segment in segments:
    req_segment = request.quote(segment.encode('cp1251'))
    
    for corpus in corpora:
        out_file = open(segment+"_"+corpus+".txt","a+")
        
        url1 = "https://search1.ruscorpora.ru/search.xml?sort=gr_tagging&out=normal&dpp=50&spd=100&seed=15490&env=alpha&mycorp=&mysent=&mysize=&mysentsize=&mydocsize=&text=lexgramm&mode="+corpus+"&lang=ru&nodia=1&parent1=0&level1=0&lex1=*"+segment+"&gramm1=A&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=&gramm2=&sem2=&sem-mod2=sem&sem-mod2=sem2&flags2=&m2=&p=0"
        print(url1)
        
        #get number of pages for each segment in each corpus
        try:
            response1 = requests.get(url1)
            soup1 = BeautifulSoup(response1.text, "html.parser")
            stats = soup1.find_all("span", {"class": "stat-number"})
            entries = stats[3].text
            entries = re.sub(" ", "", entries)
            entries = re.sub("[^0-9]", "", entries)
            pages = (int(entries) // 50) + 1
            print("number of pages for", segment, "in", corpus, "equals", pages)
        except:
            print("no entries found for", segment, "in", corpus)
            continue
            
        #get examples from each page for each segment
        for g in range(0, int(pages)):
            #print(g)
            url2 = "https://search1.ruscorpora.ru/search.xml?sort=gr_tagging&out=normal&dpp=50&spd=100&seed=15490&env=alpha&mycorp=&mysent=&mysize=&mysentsize=&mydocsize=&text=lexgramm&mode="+corpus+"&lang=ru&nodia=1&parent1=0&level1=0&lex1=*"+segment+"&gramm1=A&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=&gramm2=&sem2=&sem-mod2=sem&sem-mod2=sem2&flags2=&m2=&p="+str(g)
            #url_new = "https://processing.ruscorpora.ru/search.xml?dpp=100&format=html&g=i_doc&kwsz=5&lang=ru&level1=0&lex1=*"+segment+"&mode="+corpus+"&nodia=1&out=normal&p="+str(g)+"&parent1=0&sampling=1&seed=6975&sem-mod1=sem&sort=i_grtagging&spd=100&spp=50&sr=1&text=lexgramm"
            #print(url2)
            try:
                response2 = requests.get(url2)
                #print(g,response2)
                soup2 = BeautifulSoup(response2.text, "html.parser")
                #print(soup2.prettify())
                lemmas = soup2.find_all("table")
                lemma_table = lemmas[-1] #showing the last (lemmas) table
                lemmas = [[d.text for d in r.findAll('td')] for r in lemma_table.findAll('tr')]
                lemmas = "\n".join("\t".join(item for item in line) for line in lemmas)
                lemmas = re.sub(r'Леммы\n','',lemmas) #removing Леммы mention
                #print(lemmas)
                print("writing entries found for", segment, "in", corpus, "at page", g)
                out_file.write(lemmas+"\n")
            except:
                print("no table found for", segment, "in", corpus, "at page", g)
                #print(g)
                continue