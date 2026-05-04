class A:
 def greet(self):
  print("Hi from A")
class B:
 def greet(self):
  print("Hi from B")
class C(A, B):
    def greet(self):
      B.greet(self)
obj = C()
obj.greet()