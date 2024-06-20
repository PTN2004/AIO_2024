import random

class Stack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__stack = []
    
    def is_empty(self):
        return len(self.__stack) == 0
    
    def is_full(self):
        return len(self.__stack) == self.__capacity

    def push(self, value):
        if self.is_full():
            print("Stack is full")
        else:
            self.__stack.append(value)
    
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        else:
            return self.__stack.pop()
    
    def top(self):
        return self.__stack[len(self.__stack) - 1]
    
stack = Stack(5)
stack.push(1)
stack.push(2)

print(stack.is_full())
print(stack.top())
print(stack.pop())
print(stack.top())
print(stack.pop())
print(stack.is_empty())

print("====Stack with random value====")
for i in range(5):
    stack.push(random.randint(1,10))

print(stack.is_full())
for i in range(5):
    print(stack.top())
    print(stack.pop())

print(stack.is_empty())
