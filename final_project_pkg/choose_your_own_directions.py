import time
from threading import Timer


def directions():
    print("\nYou've made it to your first battle!\nChoose your choice wisely, for one is correct, and the other will bring you a terrible fate. Your CHOICE will be the all uppercase word.\nGood Luck!")
    time.sleep(8)


def redo():
    redo = input("Do you want to try again? Please type YES or NO ")
    if redo.upper() == "YES":
        return
    elif redo.upper() == "NO":
        print("K bye.")
        exit()
    else:
        print("What?")


def king_directions():
    print("\nYou are at the final battle against the evil King Banking App.\nYou must successfully register, login, and then donate $20,000 to the King.\nIt's lucky you had your trusty wallet of $20,000 on you")
    time.sleep(8)


def bat_directions():
    print("\nYou are at the final battle against the Giant Fruit Donation Bat.\nYou must successfully register, login, and then donate MANGOES to the Bat.\nIt's lucky you had your trusty bag of mangoes on you")
    time.sleep(8)


def game_end():
    print("Your journey has come to an end, You did it. The end")
    exit()
