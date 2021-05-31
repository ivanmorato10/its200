#################################################################
# File name:ex11_assignemnt.py                                  #
# Author: Ivan Morato                                           #
# Date:5-26-2021                                                #
# Classes:  ITS 220: Programming Languages & Concepts           #
# Instructor:Matthew Loschiavo                                  #
#  simple game that teaches kindergartners                      #
#  how to add single-digit numbers.                             #
#                                                               #
#################################################################

print("Hello kids,How are u today? Let's learn some math!!!!")

#variables declaration
y = 0
x = 0
z = 0
soma = 0
again = 0

#first imput validation
while again == 0 :
    try:
        y = int(input("First Number: "))
        if y > 0 or y > 10:
            break
        print('Come on, enter a number from 1 to 10')
    except ValueError:
        print('Are you sure? This is a number?')

#second imput validation
while True:
    try:
        x = int(input("Second Number: "))
        if x > 0 or x > 10:
            break
        print('Come on, enter a number from 1 to 10')
    except ValueError:
        print('Are you sure? This is not a number?')

soma = x + y
while soma != z:

    print("What is the sum of", x, "+", y, "??")
    # third input validation

    while True:
        try:
            z = int(input("Guess"))
            break
        except ValueError:
            print('Are you sure? This is not a number?')

    if soma == z: #Validation if the answer is correct
        print("You're right! You are the best student in the world!")
    else:
        print("We're almost there,Try again!")

print("See u next class =) ") #end