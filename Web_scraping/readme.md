# Web scraping scripts

## `get_adj.py` 

*Gets a list of adjectives from old version of Ruscorpora*

**Input**

- `corpora.txt`: the list of subcorpora to extraxt adjectives from
- `segments.txt`: the list of final segments of adjectives to extract
- `prefix.txt`: the list of caracters to search before each segment

**Output**

- A .txt file per segment & corpus with: 

    - Adjectival lemma
    - Lemma count

## `get_freq.py` 

*Gets token frequencies for given words from old version of Ruscorpora*

**Input**

- `corpora.txt`: the list of subcorpora to extraxt adjectives from
- `word_list.txt`: the list of words for which frequencies should be extracted from each subcorpora

**Output**

- `out.txt`: a file with words and their frequencies per each subcorpus

## `get_context.py`

*Gets contexts for each word from old version of Ruscorpora*

**Input**

- `word_list.txt`: list of words for which the context should be extracted

**Output**

- A .txt file per word with all the contexts availble on the page
