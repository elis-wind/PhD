import itertools
import glob
import regex as re
import pandas as pd

for file in glob.glob("*.txt"): 
    data = []
    results = []
    with open(file) as f:
        f_name = re.sub(r"\.txt", r"", file)
        print("PROCESSING",f_name,"\n")
        corpus_name = re.sub(r"_.*$", r"", f_name)
        f_name = re.sub(r"^.*_", r"", f_name)
        lemm = re.sub("..$", "", f_name)
        #print(f_name)
        lines = f.read().splitlines()
    for line in lines: #read lines except for the first (title)
        line = line.split('  ←…→')
        data.append(line)
    corpus = list(itertools.chain.from_iterable(data))
    
    ### Get rid of duplicated titles
    corpus_clean = [i for i in corpus if "Все примеры" not in i]
    
    ### Find and extract years
    regex = re.compile(r'(\d{4})')
    
    for sentence in corpus_clean: 
        for match in re.findall(regex, sentence):
            results.append(match)

    df = pd.DataFrame(results, columns = ['YEAR'])
    df.to_csv("year/{}_{}.csv".format(f_name,corpus_name),sep="\t",index=False)