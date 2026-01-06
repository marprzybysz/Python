class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def say_hello(self):
        print("Hello {}!".format(self.name))
    
    def weight(self):
        print("Your weight is {}".format(self.weight))


marcin = Person('Marcin')
marcin.say_hello()
marcin.weight()