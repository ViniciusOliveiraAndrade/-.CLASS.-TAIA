from sklearn.feature_extraction.text import TfidfVectorizer
from ControleCSV import pegarCorpus
#Corpus 
corpus = pegarCorpus()
	
vectorizer = TfidfVectorizer()
vectorizer.fit_transform(corpus) 

print(vectorizer)