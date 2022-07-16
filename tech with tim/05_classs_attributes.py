class Person:
    number_of_people = 0
    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1
p1 = Person("tim")
# p2 = Person("bill")
Person.number_of_people = 8#here we can change a attribute by referring to the class
print(Person.number_of_people)#specific to class not an instance
p2 = Person("bill")
# print(p2.number_of_people)#what this does is that first it checks deos instance have an attribute like that if no then it checks the class if yes displays it
print(Person.number_of_people)