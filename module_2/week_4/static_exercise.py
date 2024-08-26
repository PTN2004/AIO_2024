import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

data = pd.read_csv('module_2/week_4/vi_text_retrieval.csv')

context = data['text']
context = [doc.lower() for doc in context]

tfidfvectorizer = TfidfVectorizer()
context_embeding = tfidfvectorizer.fit_transform(context)

print(context_embeding.toarray()[7][0])