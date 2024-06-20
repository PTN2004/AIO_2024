import torch.nn
import math


class Softmax(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def sum_exp(self, data):
        self.value_sum = 0
        for x in data:
            self.value_sum += math.exp(x)

    def forward(self, data):
        self.sum_exp(data)

        self.output = []
        for x in data:
            softmax_value = math.exp(x)/self.value_sum
            self.output.append(softmax_value)
        return torch.tensor(self.output)


class softmax_stable(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def sum_exp(self, data):
        self.max = max(data)
        self.value_sum = 0

        for x in data:
            self.value_sum += math.exp(x - self.max)

    def forward(self, data):
        self.sum_exp(data)

        self.output = []
        for x in data:
            softmax_value = math.exp(x - self.max)/self.value_sum
            self.output.append(softmax_value)
        return torch.tensor(self.output)


data = torch.tensor([1, 2, 3])
softmax = Softmax()
result = softmax(data)

print(f"softmax 1: {result}")

data = torch.tensor([-1, -2, 3])
softmax = Softmax()
result = softmax(data)

print(f"softmax 2: {result}")


data_stable = torch.tensor([1, 2, 3])
softmax_stable = softmax_stable()
result = softmax_stable(data_stable)

print(f"softmax stable: {result}")
