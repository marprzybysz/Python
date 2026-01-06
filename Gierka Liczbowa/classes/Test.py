import Person

class Test:
    def __init__ (self):
        self.name_board = [
            "Ola", "Wiktoria", "Mateusz"
        ]
        self.weight_board = [
            80, 60, 40
        ]
        self.age_board = [
            18, 28, 30
        ]

test = Test()

person1 = Person(
  test.name_board[0], test.weight_board[0], test.age_board[0]
    )
    
person2 = Person(
  test.name_board[1], test.weight_board[1], test.age_board[1]
    )

person3 = Person(
  test.name_board[2], test.weight_board[2], test.age_board[2]
    )

person1.say_hello()
person1.say_weight()
person1.say_age()
print("\n")

person2.say_hello()
person2.say_weight()
person2.say_age()
print("\n")

person3.say_hello()
person3.say_weight()
person3.say_age()
print("\n")