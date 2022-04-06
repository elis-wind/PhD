# Data Costitution scripts

## `adjectives.py` 

*Gets raw tables of adjectives + frequencies from Web Scraping*

**Input**

- A folder with .txt file per segment & corpus with: 

    - Adjectival lemma
    - Lemma count

**Output**

- A folder with .csv file per segment & corpus with: 

    - Dropped duplicates

## `doublets.py` 

*Gets ...*

**Input**

- ...

**Output**

- ...

## `dependency_parsing.py` 

*Gets all nouns with are modified by an adjective in question from extracted contexts from Ruscorpora*

**Input**

- `corpus_adjective.txt`: contexts for adjective from a particular corpus

**Output**

- A .csv file per adjective & corpus with: 

    - Adjective
    - Modified Noun
    - Corpus

## `datetime.py` 

*Gets all years for each token for a given lemma from extracted contexts from Ruscorpora*

**Input**

- `corpus_adjective.txt`: contexts for adjective from a particular corpus

**Output**

- A .csv file per adjective & corpus with: 

    - Year