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

#read every word in txt file
for segment in segments:
    req_segment = request.quote(segment.encode('cp1251'))
    
    for corpus in corpora:
        out_file = open(corpus+"_"+segment+".txt","a+")
        
        url1 = "https://processing.ruscorpora.ru/search.xml?dpp=100&format=html&g=i_doc&kwsz=5&lang=ru&level1=0&lex1=*"+segment+"&mode="+corpus+"&nodia=1&out=normal&p=0&parent1=0&sampling=1&seed=6975&sem-mod1=sem&sort=i_grtagging&spd=100&spp=50&sr=1&text=lexgramm"
        print(url1)
        
        #get number of pages for each word
        try:
            response1 = requests.get(url1)
            soup1 = BeautifulSoup(response1.text, "html.parser")
            stats = soup1.find_all("span", {"class": "stat-number"})
            entries = stats[2].text
            entries = re.sub(" ", "", entries)
            entries = re.sub("[^0-9]", "", entries)
            pages = (int(entries) // 50) + 1
            print("number of pages for", segment, "in", corpus, "equals", pages)
        except:
            print("no entries found for", segment, "in", corpus)
            continue
            
        #get examples from each page for each word
        for g in range(0, int(pages)):
            #print(g)
            url2 = "https://processing.ruscorpora.ru/search.xml?dpp=100&format=html&g=i_doc&kwsz=5&lang=ru&level1=0&lex1=*"+segment+"&mode="+corpus+"&nodia=1&out=normal&p="+str(g)+"&parent1=0&sampling=1&seed=6975&sem-mod1=sem&sort=i_grtagging&spd=100&spp=50&sr=1&text=lexgramm"
            #print(url2)
            try:
                response2 = requests.get(url2)
                print(g,response2)
                soup2 = BeautifulSoup(response2.text, "html.parser")
                #print(soup2.prettify())
                lemmas = soup2.find_all("table")
                lemma_table = lemmas[-1] #showing the last (lemmas) table
                lemma_table = re.sub(r'Леммы','',lemma_table.text) #removing Леммы mention
                lemma_table = re.sub(r'\n',' ',lemma_table) #removing empty lines
                lemma_table = re.sub(r'  [а-я]*  ',' ',lemma_table) #removing nouns
                lemma_table = re.sub(r' [а-я]*  ',' ',lemma_table) #removing nouns
                lemma_table = re.sub(r'([0-9])\s+([0-9])',r'\1\n\2',lemma_table) #splitting lines
                lemma_table = re.sub(r'\s{2,4}','',lemma_table) #removing extra white spaces
                lemma_table = re.sub(r'([а-я])([0-9])',r'\1\n\2',lemma_table) #fixing new lines
                lemma_table = re.sub(r'([0-9]* )([а-я]* )([0-9]*).*',r'\1\2\3\n',lemma_table) #fixing end of line issues
                #print(lemma_table)
                out_file.write(lemma_table)
            except:
                continue