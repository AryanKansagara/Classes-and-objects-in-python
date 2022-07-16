class Person:
    number_of_people = 0
    def __init__(self, name):
        self.name = name
        Person.add_person()
    
    @classmethod
    def number_of_people_(cls):#class specific not intance specific
        return cls.number_of_people
        
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person("tim")
p2 = Person("bill")
print(Person.number_of_people)