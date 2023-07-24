# Data Constitution scripts

## `no_duplicates.py` 

*Drops duplicates for tables of adjectives + adds frequencies*

**Input**

- A folder with .txt file per segment & corpus (from Web Scraping) with: 

    - Adjectival lemma
    - Lemma count

**Output**

- A folder with .csv file per segment & corpus with: 

    - Dropped duplicates

## `open_url.py` 

*Searches words from a list in the main corpus of RusCorpora and opens pages with results in a browser*

**Input**

- `word_list.txt` file with the list of words to query

**Output**

- open web pages with the result of each query in the main corpus of RusCorpora

## `dependency_parsing.py` 

*Gets all nouns with are modified by an adjective in question from extracted contexts from Ruscorpora*

**Input**

- `corpus_adjective.txt`: contexts for adjective from a particular corpus

**Output**

- A .csv file per adjective & corpus with: 

    - Adjective
    - Modified Noun
    - Corpus