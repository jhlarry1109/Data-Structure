class Deque:
  li = [0] * 20
  rear, front = 0, 0

  def append(self, a):
    if self.is_full():
      return "꽉 참"
    self.li[self.rear] = a
    self.rear = (self.rear + 1) % len(self.li)
        
  def appendleft(self, a):
    if self.is_full():
      return "꽉 참"
    self.front = (self.front - 1) % len(self.li)
    self.li[self.front] = a
        
  def popleft(self):
    if self.is_empty():
      return "비어있음"
    val = self.li[self.front]
    self.front = (self.front + 1) % len(self.li)
    return val
        
  def pop(self):
    if self.is_empty():
      return "비어있음"
    self.rear = (self.rear - 1) % len(self.li)
    return self.li[self.rear]

  def is_empty(self):
    return self.rear == self.front
  
  def is_full(self):
    return self.rear == 20-1

deque = Deque()
deque.append(3)
deque.append(5)
deque.appendleft(7)
deque.appendleft(9)
deque.append(10)
deque.append(9)
print(deque.popleft())
print(deque.pop())
print(deque.popleft())
print(deque.pop())