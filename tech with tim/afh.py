
class Pet:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    def show(self):
        print(f"i am {self.name} and i am {self.age} years old")

class Cat(Pet):
    def speak(self):
        print("meow")

class Dog(Pet):
    def speak(self):
        print("bark")

p = Pet("tim",19)
p.show()
