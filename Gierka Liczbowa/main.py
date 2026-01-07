import random

# Zmienne podstawowe 
random_number = random.randint(1, 10)
user_trails = 7
user_trails_counter = 1 

# Input do gry
user_guess = int(input(f"Zgadnij liczbę od 1 do 10: \n(Masz {user_trails + 1} prób!)\nWpisz ponownie liczbę: "))

# Pętla gry
while user_trails >= 1 and user_guess != random_number:
    user_trails -= 1
    user_trails_counter += 1 
    if user_guess < random_number:
        print("Za mała liczba! Spróbuj ponownie!")
    else:
        print ("Za duża liczba Spróbuj ponownie!")
    user_guess = int(input(f"Pozostało: {user_trails + 1}\nWpisz ponownie liczbę: "))

# Rozstrzygnięcie gry
if user_trails >= 1:
    print(f"Udało ci się zgadnąć liczbę w {user_trails_counter} próbach! Gratulacje :O")
else:
    print(f"Niestety nie udało ci odgadnąć liczby. Prawidłowa liczba to {random_number}")
