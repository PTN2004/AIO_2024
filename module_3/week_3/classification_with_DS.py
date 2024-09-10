from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Load data
iris_X, iris_y = load_iris(return_X_y=True)

# Split data train:test 8:2
train_X, test_X, train_y, test_y = train_test_split(iris_X, iris_y,
                                                    test_size=0.2,
                                                    random_state=42)

# Define model
decision_tree = tree.DecisionTreeClassifier(max_depth=4)

# Train model
decision_tree.fit(train_X, train_y)

# Visualization DS model
tree.plot_tree(decision_tree)
plt.show()

# Predict and evaluate
y_predict = decision_tree.predict(test_X)
score_model = accuracy_score(test_y, y_predict)