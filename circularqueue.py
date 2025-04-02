class CircularQueue:
  li = [0] * 5
  rear, front = 0, 0

  def enqueue(self, a):
    if self.is_full():
      return "꽉 참"
    else:
      self.li[self.rear % len(self.li)] = a
      self.rear += 1
        
  def dequeue(self):
    if self.is_empty():
      return "비어있음"
    else:
      self.front += 1
      return self.li[(self.front - 1) % len(self.li)]

  def is_empty(self):
    return self.rear == self.front
  
  def is_full(self):
    return (self.rear+1)%len(self.li) == self.front%len(self.li)

queue = CircularQueue()
queue.enqueue(3)
queue.enqueue(2)

print(queue.dequeue())
print(queue.dequeue())

queue.enqueue(1)
queue.enqueue(3)
queue.enqueue(5)
queue.enqueue(8)

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
