class Queue:
  li = [0] * 20
  rear, front = -1, -1

  def insert(self, a):
    if self.is_full() == True:
      print("꽉 참")
    else:
      self.rear += 1
      self.li[self.rear] = a
  def pop(self):
    if self.is_empty():
      print("비어있음")
    else:
      self.front += 1
      return self.li[self.front]

  def is_empty(self):
    return self.rear == self.front
  
  def is_full(self):
    return self.rear == 20-1

queue = Queue()
queue.insert(3)
queue.insert(5)
queue.insert(12)
print(queue.pop())
print(queue.pop())
print(queue.pop())