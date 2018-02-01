import codecs
from nltk import pos_tag
from nltk import word_tokenize
from nltk.stem.snowball import FrenchStemmer
import os
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

###############################################################################
# DATA
###############################################################################

DATA_FILES = [
	"cv_05-08.txt",
	"cv_77-88.txt",
	"cv_83-96.txt",
	"cv_88-90.txt",
	"cv_77-88.txt",
	"cv_90-93.txt",
	"cv_77-88.txt",
	"cv_90.txt",
	"cv_96-98.txt",
	"cv_96.txt",
	"cv_98-03.txt"]
DATA_DIRECTORY = "../data"

###############################################################################
# LOAD DATA
###############################################################################

corpus = []

for file_name in DATA_FILES:
	file_path = os.path.join(DATA_DIRECTORY, file_name)
	with codecs.open(file_path, 'r', 'utf-8') as f:
		corpus.append(f.read())

###############################################################################
# COMMON WORDS
###############################################################################

stopwords = []

with codecs.open('stopwords-fr.txt') as stopwords_file:
	stopwords_text = stopwords_file.read()
	stopwords = stopwords_text.split('\n')

###############################################################################
# TOKENIZE
###############################################################################

corpus_tokenized = [word_tokenize(text.lower(), language='french') for text in corpus]

###############################################################################
# TAG
###############################################################################

corpus_tagged = [[pos_tag(token) for token in token_list] for token_list in corpus_tokenized]

###############################################################################
# STEM WORDS
###############################################################################

stemmer = FrenchStemmer(ignore_stopwords=True)
corpus_stemmed = [' '.join([stemmer.stem(token) for token in token_list]) for token_list in corpus_tokenized]

###############################################################################
# MOST MEANINGFUL WORDS
###############################################################################

tf_idf = TfidfVectorizer(
	input='content',
	encoding='utf-8',
	analyzer='word',
	max_features=40,
	stop_words=stopwords)

feature_matrix = tf_idf.fit_transform(corpus_stemmed)
feature_matrix.toarray()

###############################################################################
# TESTS
###############################################################################

print len(stopwords)
print tf_idf.get_feature_names()