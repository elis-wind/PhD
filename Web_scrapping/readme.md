# Web scrapping scripts

1. `get_adj.py` 

*Gets a list of adjectives from old version of Ruscorpora*

**Input**

- `corpora.txt`: the list of subcorpora to extraxt adjectives from
- `segments.txt`: the list of final segments of adjectives to extract

**Output**

- A .csv file per corpus & segment with: 

    - Lemma of adjective
    - Lemma count

2. `get_adj_context.py`

*Gets contexts for each adjective from old version of Ruscorpora*

**Input**

- Link personalized with:

    - a given final segment of an adjective (default \*ный)
    - number of documents per page (default 100)
    - number of examples per document (default 100)

- Total number of pages for a given segment (default 1037 for \*ный)

**Output**

- A file per final segment with all the contexts availble on the page

3. `get_nn_context.py`

*Gets contexts for each base noun from old version of Ruscorpora*

**Input**

- List of nouns

**Output**

- A .txt file per noun with all the contexts availble on the page
