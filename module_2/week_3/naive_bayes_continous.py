import numpy as np
import math

def gauss(x, mean, varian):
    std_de = np.sqrt(varian)
    result = (1/np.sqrt(2*np.pi)*std_de)*np.exp(-(-float(x) - mean)**2/varian)
    return result

def create_train_data():
    train_data = np.loadtxt('module_2/week_3/iris.data.txt', delimiter=',', dtype=str)

    return train_data

def compute_prior_probability(train_data):
    y_unique = np.unique(train_data[:, 4])
    print(y_unique)
    prior_probability = np.zeros(len(y_unique))
    for i in range(len(y_unique)):
        prior_probability[i] = len(np.where(train_data[:,4] == y_unique[i])[0])/ len(train_data)

    return prior_probability

def compute_conditional_probability(train_data):
    y_unique = np.unique(train_data[:,4])
    conditional_probability = []
    list_x_name = []
    for i in range(train_data.shape[1]-1):
        x_conditional_probability = np.zeros((len(y_unique), 2))
        for j in range(len(y_unique)):
            mean = np.mean(train_data[:,i][np.where(train_data[:,4] == y_unique[j])].astype(float))
            sigma = np.std(train_data[:,i][np.where(train_data[:,4] == y_unique[j])].astype(float))
            sigma = sigma ** sigma
            x_conditional_probability[j] = [mean, sigma]

        conditional_probability.append(x_conditional_probability)
        return conditional_probability

def train_model_naive_bayes(train_data):
    prior_probability = compute_prior_probability(train_data)
    conditional_probability = compute_conditional_probability(train_data)

    return prior_probability, conditional_probability

def predict_model_bayes(x, prior_probability, conditional_probability):
    p_x0 = prior_probability[0] * gauss()

data = create_train_data()

conditional_probability = compute_conditional_probability(data)
print(conditional_probability)

def gaussian_function(data, mean, var):
    return (1.0/np.sqrt(2*math.pi*var)) * np.exp(-(data-mean)**2 / (2*var))

gauss_lenght = gaussian_function(5.5, 6.2, 0.4**2)
gauss_width = gaussian_function(3, 2.9, 0.3**2)
P = gauss_lenght*gauss_width*0.5
print(gauss_lenght, gauss_width, P)