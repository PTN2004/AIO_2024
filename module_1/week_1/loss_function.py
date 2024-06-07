import math
import random
import sys

def MAE (number_samples):
    sum_all_loss = 0
    results = []
    for _ in range(number_samples):
        y_target = random.uniform(0,10)
        y_predict = random.uniform(0,10)
        loss = abs(y_target - y_predict)
        results.append([y_predict, y_target, loss])
        sum_all_loss += loss
    
    final_loss = sum_all_loss/number_samples
    return results, final_loss

def MSE (number_samples):
    sum_all_loss = 0
    results = []
    for _ in range(number_samples):
        y_target = random.uniform(0,10)
        y_predict = random.uniform(0,10)
        loss = (y_target - y_predict)**2
        results.append([y_predict, y_target, loss])
        sum_all_loss += loss
    
    final_loss = sum_all_loss/number_samples
    return results, final_loss
    
def RMSE (number_samples):
    _ , final_loss = MSE(number_samples)
    return math.sqrt(final_loss)

def output(results, final_loss, loss_name):
    sample = 0
    for result in results:           
        print(f"Loss name: {loss_name}, sample: {sample}, predict: {result[0]}, target: {result[1]}, loss: {result[2]}")
        sample += 1
    print('=> final loss: ', final_loss)


#--------------------------

number_sample_input = input('Input number of samples (integer number) which are generated: ')

if not number_sample_input.isnumeric():
    print('* Number of samples must be an integer number')
    sys.exit()

number_samples = int(number_sample_input)
loss_name = input('Input loss name (MAE, MSE): ')

if loss_name.lower() == 'mae':
    results, final_loss = MAE(number_samples)
    output(results, final_loss, loss_name)
elif loss_name.lower() == 'mse':
    print('Processing...')
    results, final_loss = MSE(number_samples)
    output(results, final_loss, loss_name)
else:
    print('Error')
        
        

