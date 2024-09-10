from sklearn.datasets import fetch_openml
from sklearn import tree
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Load data
machine_cpu = fetch_openml(name='machine_cpu')
machine_data = machine_cpu.data
machine_label = machine_cpu.label

# Split data train:test 8:2
X_train, X_test, y_train, y_test = train_test_split(machine_data, machine_label,
                                                    test_size=0.2, random_state=42)
# Define model decision tree
decision_tree = tree.DecisionTreeRegressor()

# Train model
decision_tree.fit(X_train, y_train)

# Visualization model DT
tree.plot_tree(decision_tree)
plt.show()

# Predict and evaluate
y_predict = decision_tree.predict(X_test)
score = mean_squared_error(y_test, y_predict)
print(score)
