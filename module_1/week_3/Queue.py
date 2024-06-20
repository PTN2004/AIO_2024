class Queue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []

    def is_empty(self):
        return len(self.__queue) == 0

    def is_full(self):
        return len(self.__queue) == self.__capacity

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        else:
            return self.__queue.pop(0)

    def enqueue(self, value):
        if self.is_full():
            print("Queue is empty")
        else:
            self.__queue.append(value)

    def font(self):
        return self.__queue[0]


queue = Queue(5)

queue.enqueue(1)
queue.enqueue(2)

print(queue.is_full())
print(queue.font())
print(queue.dequeue())
print(queue.font())
print(queue.dequeue())
print(queue.is_empty())

print("====Queue with random value====")
for i in range(5):
    queue.enqueue(i)

print(queue.is_full())
for i in range(5):
    print(queue.font())
    print(queue.dequeue())

print(queue.is_empty())
