
class Pet:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    def show(self):
        print(f"i am {self.name} and i am {self.age} years old")

class Cat(Pet):
    def __init__(self, name, age, color):
        self.color = color
        super().__init__(name, age)
    def speak(self):
        print(f"i am {self.name} and i am {self.age} years old and i am {self.color}")

class Dog(Pet):
    def speak(self):
        print("bark")

p = Pet("tim",19)
p.show()
c = Cat("billy",34,"brown")
c.speak()