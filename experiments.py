
import locale

# Regionally set the locale
locale.setlocale(locale.LC_ALL, '')

def input_float(prompt):
    while True:
        try:
            user_input = input(prompt)
            user_input = locale.atof(user_input)
            return user_input
        except ValueError:
            print("Incorrect input. Please enter a number.")

'''
this is for testing the input_float function
user_number = input_float("Provide a number: ")
print(f"You provided number: {user_number}")
'''

# Mini-program with options to choose from

choose = input("What do you want to calculate, distance or weight? ")
if choose == "distance":
    choose_distance = input('Convert kilometers to miles or miles to kilometers? ')
    if choose_distance == "kilometers to miles":
        kilometers = float(input("Enter the number of kilometers: "))
        print("That is {} miles".format(kilometers/1.61))
    elif choose_distance == "miles to kilometers":
        miles = float(input("Enter the number of miles: "))
        print("That is {} kilometers".format(miles*1.61))
if choose == "weight":
    choose_weight = input("Convert kilograms to pounds or pounds to kilograms? ")
    if choose_weight == "kilograms to pounds":
        kilograms = float(input("Enter the number of kilograms: "))
        print("That is {} pounds".format(kilograms*2.205))
    elif choose_weight == "pounds to kilograms":
        pounds = float(input("Enter the number of pounds: "))
        print("That is {} kilograms".format(pounds*0.2205))

