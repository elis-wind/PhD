import os
import glob
import regex as re
import pandas as pd
import spacy

rus = spacy.load('ru_core_news_sm')

for file in glob.glob("*.txt"): 
    data = []
    results = []
    with open(file) as f:
        f_name = re.sub(r"\.txt", r"", file)
        print("PROCESSING",f_name,"\n")
        corpus = re.sub(r"_.*$", r"", f_name)
        f_name = re.sub(r"^.*_", r"", f_name)
        lemm = re.sub("..$", "", f_name)
        #print(f_name)
        lines = f.readlines()
    for line in lines[1:]: #read lines except for the first (title)
        #line = line.split('  ←…→')
        #line = re.sub(r"\s*\[.*$", r"", line).lower()
        data.append(line)
    for ex in data:
        doc = rus(ex)
        for token in doc:
            if lemm in token.text:
                results.append({"ADJ": token.lemma_, "NN": token.head.lemma_, "CORPUS": corpus})
            else:
                pass
    df = pd.DataFrame(results, columns = ['ADJ', 'NN', 'CORPUS'])
    df.to_csv("{}_{}.csv".format(f_name,corpus),sep="\t",index=False)