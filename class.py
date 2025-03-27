class C1:
  a: int
  b: int

  def __init__(self, a, b):
    self.a = a
    self.b = b
  def __str__(self):
    return f'{self.a} {self.b}'
  def m1(self):
    return self.b * self.a
  
a = C1(a:1, b:2)
print(a.m1())
class C2(C1):
  c: int
  def __init__(self, a, b):
    super().__init__(a, b)

  def m2(self):
    return self.b * self.a * self.c