import pandas as pd
import glob
from pathlib import Path

raw_r = 0 #set count for rows after extraction
unique_r = 0 #set count for rows after removing duplicates
clean_r = 0 #set count for rows after noise cleaning

for file in glob.glob("01.data_raw/*.txt"):
    f_name = Path(file).stem #get filename without folder, without extension
    corpus = f_name.split("_")[1] #get corpus name from filename
    print("\t",f_name)
    
    with open(file) as f:
        data = pd.read_csv(f, sep="\t", names = ["id","lemma","occurence"], usecols = ['lemma','occurence'])

    #DROPPING DUPPLICATES
    #data.loc[len(data)] = ["lemma",count]  #add a duplicated lemma for testing (if no duplicates in data)
    data.sort_values(by=['occurence'],ascending=False,inplace=True)
    raw_r += len(data)
    print("number of raw rows in", file, len(data))
    print("dupplicates in", file, ":", sum(data["lemma"].duplicated()))
    data[corpus] = data.groupby('lemma')['occurence'].transform('sum') #sum up occurence for duplicated lemmas
    data.drop_duplicates(subset=['lemma'],inplace=True) #drop duplicated lemmas, keep first
    unique_r += len(data)
    print("number of clean rows in", file, len(data))
    data.drop("occurence",axis=1,inplace=True) #drop occurence columns
    
    data.to_csv("02.count_clean/"+f_name+".csv",sep="\t",index=False)
    
    #REMOVING NOISE
    clean_r += len(data)
    
print("\nraw rows after extraction:", raw_r)
print("unique rows after dropping dupplicates:", unique_r)
print("clean rows after removing noise:", clean_r)