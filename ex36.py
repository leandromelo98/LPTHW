from sys import exit

def zoo():

    print "you are in zoo."
    print "what do you want to see:"
    print "snake or zebra?"
    choice = raw_input()

    if choice == "snake":
        snake()
    elif choice == "zebra":
        zebra()

def snake():

    print "you are looking at the snake now."
    print "what do you want to see next:"
    print " elephant or lion?"

    option = raw_input()

    if option == "elephant":
        elephant()
    elif option == "lion":
        lion()


def monkey():

    print "you are looking at the monkey now."
    print "what do you want to see next:"
    print "elephant or lion?"

    way = raw_input()

    if way == "elephant":
        elephant()
    if way == "lion":
        lion()


def elephant():

    print "you are looking at the elephant now."
    print "what do you want to see next:"
    print "monkey or lion?"

    road = raw_input()

    if road == "lion":
        lion()
    if road == "monkey":
        monkey()


def zebra():

    print "you are looking at the zebra now."
    print " what do you want to see next:"
    print "elephant or snake?"

    zebraway = raw_input()

    if zebraway == "elephant":
        elephant()
    if zebraway == "snake":
        snake()

def lion():

    print "you are looking at the lion now."
    print "this is the end of the zoo"
    print "hope to see you next time"

    exit(0)

zoo()
