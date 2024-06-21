class MyStack:
  def __init__(self, capacity) -> None:
    self.__capacity = capacity
    self.__data = []

  def is_full(self):
    return len(self.__data) == self.__capacity

  def is_empty(self):
    return len(self.__data) == 0

  def push(self, value):
    if self.is_full():
      print("Stack is full")
    else:
      self.__data.append(value)

  def top(self):
    if self.is_empty():
      print("Stack is empty")
    else:
      return self.__data[-1]

  def pop(self):
    if self.is_empty():
      print("Stack is empty")
    else:
      value = self.__data.pop()
      return value


stack1 = MyStack(capacity=5)

stack1.push(1)
stack1.push(2)
print(stack1.is_full())
print(stack1.top())
print(stack1.pop())
print(stack1.top())
print(stack1.pop())
print(stack1.is_empty())
