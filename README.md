# This is a data mining project on Facebook for the Advanced Topics in Artificial Intelligence class.

## Requirements

This project needs the Python version 3.7.* , nltk (tokenize,stem,corpus), sklearn (cross_validation, feature_extraction, naive_bayes, metrics, linear_model, naive_bayes, model_selection, svm ), the Graph API from Facebook.


## Introduction

This project was developed to collect data from comments on Facebook posts aiming to collect their opinion, by supervised machine learn.

## Steps

### Data Collect

The data was collected by the Graph API from Facebook, request framework from Python. 

### Preprocessing

The Graph response was cleaned by regular expression, stemming, and sotp-word, URL, special characters removal.
Then, they were tokenazed, so they could be easily used for training the machine.

### Processing

To process the polarity classification of the data, and analyze it, were used the Naıve-Bayes algorithm, Countvectorizer, Tfidfvectorizer, Kfold, SVC Linear, and the Logistic Regression algorithm.