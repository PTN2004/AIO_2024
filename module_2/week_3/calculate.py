import numpy as np
import math


def mean(data):
    return sum(data)/len(data)


def variance(data, value_mean=None):
    if value_mean == None:
        value_mean = mean(data=data)
    sum = 0
    for i in data:
        sum += (i - value_mean)**2
    return sum/len(data)


def gauss(data):
    mean_data = mean(data)
    var_data = variance(data, value_mean=mean_data)


def create_train_data():
    data = [['Sunny', 'Hot', 'High', 'Weak', 'no'],
            ['Sunny', 'Hot', 'High', 'Strong', 'no'],
            ['Overcast', 'Hot', 'High', 'Weak', 'yes'],
            ['Rain', 'Mild', 'High', 'Weak', 'yes'],
            ['Rain', 'Cool', 'Normal', 'Weak', 'yes'],
            ['Rain', 'Cool', 'Normal', 'Strong', 'no'],
            ['Overcast', 'Cool', 'Normal', 'Strong', 'yes'],
            ['Overcast', 'Mild', 'High', 'Weak', 'no'],
            ['Sunny', 'Cool', 'Normal', 'Weak', 'yes'],
            ['Rain', 'Mild', 'Normal', 'Weak', 'yes']]
    return np.array(data)


def compute_prior_probability(data):
    y_unique = ['no', 'yes']
    prior_probablity = np.zeros(len(y_unique))

    for i in range(len(y_unique)):
        prior_probablity[i] = len(
            np.where(data[:, 4] == y_unique[i])[0])/len(data[:, 4])

    return prior_probablity


def compute_conditional_probablity(data):
    y_unique = ['no', 'yes']
    list_x_name = []
    conditional_probability = []
    for i in range(data.shape[1] - 1):
        x_unique = np.unique(data[:, i])
        print(x_unique)
        list_x_name.append(x_unique)

        x_conditional_probability = np.zeros((len(y_unique), len(x_unique)))
        for j in range(len(y_unique)):
            for k in range(len(x_unique)):
                x_conditional_probability[j, k] = len(np.where((data[:, i] == x_unique[k]) & (
                    data[:, 4] == y_unique[j]))[0]) / len(np.where(data[:, 4] == y_unique[j])[0])
                print(f"j = {j}, k = {k} x_conditional_probability= {
                      x_conditional_probability[j, k]}")
        conditional_probability.append(x_conditional_probability)
    return list_x_name, conditional_probability


def get_index_from_value(feature_names, list_features):
    return np.where(list_features == feature_names)[0][0]


def train_naive_bayes_model(train_data):

    prior_probability = compute_prior_probability(train_data)
    list_x_names, conditional_probability = compute_conditional_probablity(
        train_data)
    return prior_probability, conditional_probability, list_x_names


def predict_naive_bayes_model(X, prior_probability, conditional_probability, list_x_names):
    x0 = get_index_from_value(X[0], list_x_names[0])
    x1 = get_index_from_value(X[1], list_x_names[1])
    x2 = get_index_from_value(X[2], list_x_names[2])
    x3 = get_index_from_value(X[3], list_x_names[3])

    p0 = (prior_probability[0] * conditional_probability[0][0][x0] * conditional_probability[1]
          [0][x1] * conditional_probability[2][0][x2] * conditional_probability[3][0][x3])
    p1 = (prior_probability[1] * conditional_probability[0][1][x0] * conditional_probability[1]
          [1][x1] * conditional_probability[2][1][x2] * conditional_probability[3][1][x3])

    if p0 > p1:
        y_predict = 0
    else:
        y_predict = 1

    return y_predict




data = create_train_data()


X = ['Sunny', 'Cool', 'High', 'Strong']
p, con, lx = train_naive_bayes_model(data)

print(predict_naive_bayes_model(X, p, con, lx))
# print(get_index_from_value('Overcast', lx[0]))
