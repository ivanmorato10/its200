def make_tuna():
    tuna = input("What tuna would you like? ")
    bread = input("OK - and how about the bread? ")
    print("Thanks. Let's go!")
    print("Preparing your dish")
    print("Seasoning your " + tuna + " tuna")
    print("Now adding in the " + bread + " bread")
    print("Finished! There's your " + tuna + " and " + bread + " sandwich!")

def make_chicken():
    chicken = input("What chicken would you like? ")
    bread = input("OK - and how about the bread? ")
    print("Thanks. Let's go!")
    print("Preparing your dish")
    print("Seasoning your " + chicken + " chicken")
    print("Now adding in the " + bread + " bread")
    print("Finished! There's your " + chicken + " and " + bread + " sandwich!")

def menu():
    sanduiche = int(input("Which sandwich would you like tuna (1) or chicken (2)? "))

    if sanduiche == 1:
        make_tuna()
    elif sanduiche == 2:
        make_chicken()
    return print("Good choice")

print("Welcome to Brazilian Restaurante")

another = "Y"
while another == "Y":
    menu()
    another = input("How about another(Y/N)? ")