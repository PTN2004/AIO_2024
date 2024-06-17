import math


def is_number(x):
    try:
        float(x)
    except ValueError:
        return False
    return True


def sigmoid(x):
    return 1/(1 + math.e**-x)


def relu(x):
    if x <= 0:
        return 0
    else:
        return x


def elu(x):
    if x <= 0:
        return 0.01*(math.e**x - 1)
    else:
        return x


def activation_function():
    x_input = input('Input x = ')

    if is_number(x_input):
        x = float(x_input)
        activation_function = input(
            'Input activation function (sigmoid | relu |elu): ')
        if activation_function.lower() == 'sigmoid':
            result = sigmoid(x)
            print(f'sigmoid: f({x}) = {result}')

        elif activation_function.lower() == 'relu':
            result = relu(x)
            print(f'relu: f({x}) = {result}')

        elif activation_function.lower() == 'elu':
            result = elu(x)
            print(f'elu: f({x}) = {result}')
        else:
            print(f'{activation_function} is not supportted')
    else:
        print('x must be number')


activation_function()

while True:
    print("1/Continue     2/exit")
    choose = input("Enter your choose: ")
    if choose == '2':
        break
    activation_function()
print("____End____")
