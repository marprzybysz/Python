class Person:
    def __init__(self, name, weight, age):
        self.name = name
        self.weight = weight
        self.age = age

    def say_hello(self):
        print("Hello {}!".format(self.name))
    
    def say_weight(self):
        print("Your weight is {}".format(self.weight))
    
    def say_age(self):
        print ("Your age is {}".format(self.age))


marcin = Person(
    input("/nWpisz imię: "),
    input("Wpisz wagę: "),
    input("Wpisz wiek: ")
    )
marcin.say_hello()
marcin.say_weight()
marcin.say_age()

