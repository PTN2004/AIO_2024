from datasets import load_dataset
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score

import numpy as np

# Load data
data = load_dataset("imdb")
data_train, data_test = data["train"], data["test"]

# Convert text to vector
vectorizer = CountVectorizer(max_features=1000)
X_train = vectorizer.fit_transform(data_train["text"]).toarray()
X_test = vectorizer.transform(data_test["text"]).toarray()
y_train = np.array(data_train["label"])
y_test = np.array(data_test["label"])

# Scale the features
scale = StandardScaler()
X_train = scale.fit_transform(X_train)
X_test = scale.transform(X_test)

# Buil KNN classifier
knn_classifier = KNeighborsClassifier(n_neighbors=1, algorithm="ball_tree")
knn_classifier = knn_classifier.fit(X_train, y_train)   # the fit method creates a K D_tree

# Predict
y_pre = knn_classifier.predict(X_test)
score = accuracy_score(y_test, y_pre)
print(score)