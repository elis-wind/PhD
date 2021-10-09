# Web scrapping scripts

`get_adj.pl` 

Copyright: [Fédéric Pont](https://github.com/FredPont)

Gets list of adjectives from Ruscorpora

**Input**

- Link personalized with:

    - a given final segment of an adjective (default \*ный)
    - number of documents per page (default 100)
    - number of examples per document (default 100)

- Total number of pages for a given segment (default 1037 for \*ный)

**Output**

- A .csv file per page with: 

    - Lemma of adjective
    - Lemma count

`get_adj_context.py`

`get_nn_context.py`
