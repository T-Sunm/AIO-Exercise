class MyQueue:
  def __init__(self, capacity) -> None:
    self.__capacity = capacity
    self.__data = []

  def is_full(self):
    return len(self.__data) == self.__capacity

  def is_empty(self):
    return len(self.__data) == 0

  def enqueue(self, value):
    if self.is_full():
      print("Queue is full")
    else:
      self.__data.append(value)

  def front(self):
    if self.is_empty():
      print("Queue is empty")
    else:
      return self.__data[0]

  def dequeue(self):
    if self.is_empty():
      print("Queue is empty")
    else:
      value = self.__data.pop(0)
      return value


queue1 = MyQueue(capacity=5)
queue1.enqueue(1)
queue1.enqueue(2)
print(queue1.is_full())
print(queue1.front())
print(queue1.dequeue())
print(queue1.front())
print(queue1.dequeue())
print(queue1.is_empty())
