# blogspot_scraper
A blog scraper for the Blogspot platform.

## Description

Project proposal for research in Sociology using Natural Language Processing.

### Objective
To demonstrate the use of data mining methods in data science to study blogs under the Blogspot platform. The gathered data can later be processed using Natural Language Processing Toolkits (e.g. summary extraction, topic modelling, etc.), or to be content analyzed using traditional social science research methods.

### Note
Most of the work can be found in the `gensim.ipynb` under the `nlp` directory. The dataset has been normalized onto a `tf-idf` model which can then be passed onto a word2vec model. 

## Tree
|Files|Description|
|:----|----------:|
|`blogspot_scraper.py`| Webscraper|
|`parser.py`|Raw text parser. Outputs `csv`|
|`blog_spot.csv`|Initial `csv` after scrape|
|`blog_tokenizer.ipynb`|Dataframe/text cleaning and testing|
|`SentimentAnalysis.ipynb`|Testing sentiment analysis application to dataset|
|`gensim.ipynb`|Applying transformations based on the Gensim library|

### Disclaimer
The initial work in Sociology technically ended after the data gathering process (scraping). Everything else after that has been a self-directed learning exercise in natural language processing. Currently, I am working through Michael Nielsen's [Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com/index.html). Hopefully I can get to a point where I can create an artificially labelled dataset to train on.

For corrections, please PM me at my git_username gmail.com email.
