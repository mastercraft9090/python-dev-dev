import sys
# This import code essentially is used to break the execution of a program when a condition is met

print("Welcome to the rollercoaster")
height=int(input("What is your height in cms: "))

if height < 120:
    print("Sorry! You cannot ride the rollercoaster")
    sys.exit()
    # This is the implemementation of the sys import above code.

age=int(input("Enter the age of the customer: "))

if height >= 120 and age >= 18:
    print("Welcome to the ride please pay $12")

elif height >= 120 and age < 18 and age >= 12:
    print("Welcome to the ride please pay $7")

elif height >= 120 and age < 12:
    print("Welcome to the ride, please pay $5")

else:
    print("Sorry! You cannot ride on the rollercoaster")
