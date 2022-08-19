import pandas as pd
import regex as re
import requests
from bs4 import BeautifulSoup
import sys
import warnings
warnings.simplefilter(action='ignore')


def phono(text):
    try:
        url = "https://ru.wiktionary.org/wiki/"+text
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')
        stress = soup.find('span', class_=['hyph','hyph-dot']).find_parent('b')

        #print(stress.get_text())
        return re.sub("·","-",stress.get_text())
    
    except:
        print("No info on {} found".format(text))
        pass


def main():
    """
    Function to get phonological data from Wikitionary
    """
    if len(sys.argv) == 4:

        data, noun, structure = sys.argv[1:]

        df = pd.read_csv(str(data), sep='\t')

        log_every = 5
        for i in range(len(df)):
            if pd.isnull(df[str(structure)][i]):
                df[str(structure)][i] = phono(df[str(noun)][i])
            else:
                pass
            if (i % log_every) == 0:
                print(i)

    df.to_csv(str(data), sep = '\t', index=False)


if __name__ == '__main__':
    main()