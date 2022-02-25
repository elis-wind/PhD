import requests
from urllib import request
import time
from bs4 import BeautifulSoup, NavigableString, Tag
from re import split
import regex as re

with open('corpora.txt', 'r') as f:
    corpora = f.read().splitlines()

with open('segments.txt', 'r') as f:
    segments = f.read().splitlines()

with open('prefix.txt') as f:
    prefix = f.read().splitlines()

#get lemma+frequency for every prefix+segment from every corpora
for corpus in corpora:
    for segment in segments:
        for pref in prefix:
            req_prefix = request.quote(pref.encode('cp1251'))
            req_segment = request.quote(segment.encode('cp1251'))
    
            out_file = open(segment+"_"+corpus+".txt","a+")
        
            url1 = "https://search1.ruscorpora.ru/search.xml?sort=gr_tagging&out=normal&dpp=50&spd=100&seed=8455&env=alpha&mycorp=&mysent=&mysize=&mysentsize=&mydocsize=&text=lexgramm&mode="+corpus+"&lang=ru&nodia=1&parent1=0&level1=0&lex1=*"+pref+segment+"&gramm1=A&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=&gramm2=&sem2=&sem-mod2=sem&sem-mod2=sem2&flags2=&m2=&p=0"
            print(url1)
        
            #get number of pages for each word
            try:
                response1 = requests.get(url1)
                soup1 = BeautifulSoup(response1.text, "html.parser")
                stats = soup1.find_all("span", {"class": "stat-number"})
                entries = stats[3].text
                entries = re.sub(" ", "", entries)
                entries = re.sub("[^0-9]", "", entries)
                pages = (int(entries) // 50) + 1
                print("number of pages for", pref,segment, "in", corpus, "equals", pages)
            except:
                print("no entries found for", pref,segment, "in", corpus)
                continue

            #get examples from each page for each word
            for g in range(0, int(pages)):
                url2 = "https://search1.ruscorpora.ru/search.xml?sort=gr_tagging&out=normal&dpp=50&spd=100&seed=8455&env=alpha&mycorp=&mysent=&mysize=&mysentsize=&mydocsize=&text=lexgramm&mode="+corpus+"&lang=ru&nodia=1&parent1=0&level1=0&lex1=*"+pref+segment+"&gramm1=A&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=&gramm2=&sem2=&sem-mod2=sem&sem-mod2=sem2&flags2=&m2=&p="+str(g)
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
                    print("writing entries found for", pref,segment, "in", corpus, "at page", g)
                    out_file.write(lemmas+"\n")
                except:
                    print("no table found for", pref,segment, "in", corpus, "at page", g)
                    continue