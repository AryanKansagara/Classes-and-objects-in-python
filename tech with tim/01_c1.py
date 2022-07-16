class Dog:
    def __init__(self,name,age):
        self.name = name#attribute
        self.age = age
        # print(self.name)#or you could also write print(name)
    
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age 
    def add_one(self, x):
        return x + 1
    
    def bark(self):
        print("bark ")
        
    def set_age(self, age):
        self.age = age
d = Dog("tim",12)
print(d.get_name())
d.set_age(232441)
print(d.get_age())

# d2 = Dog("bill",23)
# print(d2.get_name())
# print(d2.get_age())
# d.bark()
# print(d.add_one(5))
# print(type(d))