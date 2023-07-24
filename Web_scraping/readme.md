# Web scraping scripts

## `get_adj.py` 

*Gets a list of adjectives from old version of Ruscorpora*

**Input**

- `corpora.txt`: the list of sub-corpora to extract adjectives from
- `segments.txt`: the list of final segments of adjectives to extract
- `prefix.txt`: the list of characters to search before each segment

**Output**

- A .txt file per segment & corpus with: 

    - Adjectival lemma
    - Lemma count

## `get_freq.py` 

*Gets token frequencies for given words from old version of Ruscorpora*

**Input**

- `corpora.txt`: the list of sub-corpora to extract adjectives from
- `word_list.txt`: the list of words for which frequencies should be extracted from each sub-corpora

**Output**

- `out.txt`: a file with words and their frequencies per each sub-corpus

## `get_context.py`

*Gets contexts for each word from old version of Ruscorpora*

**Input**

- `word_list.txt`: list of words for which the context should be extracted

**Output**

- A .txt file per word with all the contexts available on the page
