class Dog:
 def __init__(self, name):
    self.name = name
 def speak(self):
   return "woof"
 def presentacion(self):
   return f"mi nombre es {self.name} y digo {self.speak()}"
    
dog = Dog("Bobby")
print(dog.presentacion())
