#################################################################
# File name:ex11_assignemnt.py                                  #
# Author: Ivan Morato                                           #
# Date:6-6-2021                                                #
# Classes:  ITS 220: Programming Languages & Concepts           #
# Instructor:Matthew Loschiavo                                  #
#  simple game that teaches kindergartners                      #
#  how to add single-digit numbers.                             #
#                                                               #
#################################################################


def game(): #function game

    print("Hello kids,How are u today? Let's learn some math!!!!")


    # variables declaration
    y = 0
    x = 0
    z = 0
    soma = 0
    again = 0

    # first input validation
    while True:
        try:
            y = int(input("First Number: ")) #input first number
            if y > 0 and y < 10:
                break
            print('Come on, enter a number from 1 to 10') #validation if it is a number from 0 to 9
        except ValueError:
            print('Are you sure? This is a not number!!!') #validation if it is not a letter

    # second input validation
    while True:
        try:
            x = int(input("Second Number: "))
            if x > 0 and x < 10:
                break
            print('Come on, enter a number from 1 to 10')
        except ValueError:
            print('Are you sure? This is a not number!!!')

    soma = x + y #variable soma stores the correct value
    while soma != z:

        print("What is the sum of", x, "+", y, "??")
        # third input validation

        while True:
            try:
                z = int(input("Now, Try guess: "))
                break
            except ValueError:
                print('Are you sure? This is not a number?')

        if soma == z:  # Validation if the answer is correct
            print("You're right! You are the best student in the world!")
        else:
            print("We're almost there,Try again!")

    #storing the correct answer in a txt file

    r = "\n Don't forget the sum of " + str(x) + " + " + str(y) + " is = " + str(soma)
    file = open("soma.txt", "a")
    file.write(r)
    file.close()


#checking if the student wants to play again

play_again = "Y"
while play_again == "Y":
    game()
    play_again  = input("How about another game(Y/N)? ")
    play_again  = play_again.upper()
print("See u next class =) ")