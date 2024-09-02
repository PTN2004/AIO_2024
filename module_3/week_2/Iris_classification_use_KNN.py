import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

X_iris, y_iris = datasets.load_iris(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X_iris, y_iris,
                                                    test_size=0.2,
                                                    random_state=42)

# print(len(X_train))
# print(len(X_test))

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = KNeighborsClassifier(n_neighbors=5)
model = model.fit(X_train, y_train)

y_perdict = model.predict(X_test)
score_model = accuracy_score(y_test, y_perdict)
print(score_model)