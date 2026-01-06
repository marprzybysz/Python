import random

# Zmienne podstawowe 
random_number = random.randint(1, 10)
user_trails = 5
user_trails_conter = 0 

# Input do gry
user_guess = int(input(f"Zgadnij liczbę od 1 do 10: \n(Masz {user_trails} prób!)\n"))

# Pętla gry
while user_trails > 0 and user_guess != random_number:
    user_trails -= 1
    user_trails_conter += 1
    if user_guess < random_number:
        print("Za mała liczba! Spróbuj ponownie!")
    elif user_guess > random_number:
        print ("Za duża liczba Spróbuj ponownie!")
    user_guess = int(input(f"Wpisz ponownie liczbę: \nPozostało: {user_trails}\n"))

# Rozstrzygnięcie gry
if user_trails >= 1:
    print(f"Udało ci się zgadnąć liczbę w {user_trails_conter} próbach! Gratulacje :O")
else:
    print(f"Niestety nie udało ci odgadnąć liczby. Prawidłowa liczba to {random_number}")
