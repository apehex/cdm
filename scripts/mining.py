import os
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

DATA_FILES = ["cv_05-08.txt", "cv_O5.txt"]
DATA_DIRECTORY = "../data"

corpus = []

for file_name in DATA_FILES:
	file_path = os.path.join(DATA_DIRECTORY, file_name)
	with open("file_path") as f:
		corpus.append(f.read())
