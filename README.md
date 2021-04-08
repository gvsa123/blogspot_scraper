# blogspot_scraper
A blog scraper for the Blogspot platform.

## Description

Project proposal for research in Sociology using Natural Language Processing.

### Objective
To demonstrate the use of data mining methods in data science to study blogs under the Blogspot platform. The gathered data can later be processed using Natural Language Processing Toolkits (e.g. summary extraction, topic modelling, etc.), or to be content analyzed using traditional social science methods.

### Note
Most of the work can be found in the `gensim.ipynb`. I believe I have the `tf-idf` modelling down. I recently worked on creating the similarity matrix, but I'd have to make sure.

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
This is a self-directed learning exercise, and I probably got (a lot) some things wrong. I started to learn about normalizing the data and creating the model, stopped there and uploaded the code. If there is anything blatantly obvious and you have the time, please point it out and PM me at my git_username gmail.com email. 

As of this edit, I have resumed work on this, thanks to COVID. Hopefully I can actually figure out how to get this model working with the blog_spot dataset.
