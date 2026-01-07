import random

random_number = random.randint(1, 10)
number = input("Wpisz cyfrę od 1 do 10: ")

def number(number1, number2):
    if number1  random_number:
        return "Zgadłeś liczbę!"
    elif number1 > random_number:
        return "Ta liczbą jest za duża"
    else:
        return "Ta liczba jest za mała"

if "Zgadłeś liczbę!":
    print("Zgadłeś liczbę! Gratulacje!")
elif "Ta liczbą jest za duża":
    print("\nTa liczbą jest za duża! Spróbuj ponownie!")
    input("Wpisz ponownie cyfrę od 1 do 10: ")
else:
    print("\nTa liczbą jest za mała! Spróbuj ponownie!")
    input("Wpisz ponownie cyfrę od 1 do 10: ")
