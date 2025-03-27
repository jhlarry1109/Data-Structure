class Stack:
  li = [0] * 20
  top = -1

  def insert(self, a):
    if self.is_full() == True:
      print("스택 가득 참")
    else:
      self.top += 1
      self.li[self.top] = a

  def pop(self):
    if self.is_empty() == True:
      print("스택 비었음")
    else:
      value = self.li[self.top]
      self.top -= 1
      return value
    
  def is_empty(self):
    if self.top == -1:
      return True
    else:
      return False
  
  def is_full(self):
    if self.top == 20-1:
      return True
    else:
      return False

stack = Stack()
stack.insert(3)
stack.insert(5)
stack.insert(12)
print(stack.pop())
print(stack.pop())
print(stack.pop())