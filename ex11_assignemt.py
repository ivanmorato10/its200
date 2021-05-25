#################################################################
# File name:ex11_assignemnt.py                                  #
# Author: Ivan Morato                                           #
# Date:5-22-2021                                                #
# Classes:  ITS 220: Programming Languages & Concepts           #
# Instructor:Matthew Loschiavo                                  #
# Modify the code in the Long Exercise Solution on page 32 that #          #
#                                                               #
#################################################################

print("Welcome to Brazilian Restaurant!")
guess = 0


while guess != 25:

 g = input("How old is the waitress? ")

 try:
     guess = int(g)
 except:
     print("Please enter a number")

 if guess == 25:
     print("You're right! won a discount!")
 else:
    if guess > 25:
        print("Too high,try again")
    else:
        print("Too low,try again")

print("Thank u  =) ")