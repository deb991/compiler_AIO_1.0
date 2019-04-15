#!/usr/bin/env python - i
import os
import pickle
from time import sleep

# Greeter is a terminal application that greets old friends warmly,
#   and remembers new friends.

def disp__titleBar():
    # Clears the terminal screen, and displays a title bar.
    try:
        os.system('cls')

    except:
        os.system('clear')

    print("\t**********************************************")
    print("\t*****    <<Jey>> - welcome JsOzzius!!    *****")
    print("\t**********************************************")


def get_user_choice():
    # Let users know what they can do.
    print("\n[1] See a list of friends.")
    print("[2] Tell me about someone new.")
    print("[3] Work with your Cloud !!!.")
    print("[q] Quit.")

    return input("What would you like to do? ")

def show_names():
    # Shows the names of everyone who is already in the list.
    print("\nHere are the people I know.\n")
    for name in names:
        print(name.title())

def get_new_name():
    # Asks the user for a new name, and stores the name if we don't already
    #  know about this person.
    new_name = input("\nPlease tell me this person's name: ")
    if new_name in names:
        print("\n%s is an old friend! Thank you, though." % new_name.title())
    else:
        names.append(new_name)
        print("\nI'm so happy to know %s!\n" % new_name.title())

def load_names():
    # This function loads names from a file, and puts them in the list 'names'.
    #  If the file doesn't exist, it creates an empty list.
    try:
        file_object = open('names.pydata', 'rb')
        names = pickle.load(file_object)
        file_object.close()
        return names
    except Exception as e:
        print(e)
        return []

def quit():
    # This function dumps the names into a file, and prints a quit message.
    try:
        file_object = open('names.pydata', 'wb')
        pickle.dump(names, file_object)
        file_object.close()
        print("\nThanks for playing. I will remember these good friends.")
    except Exception as e:
        print("\nThanks for playing. I won't be able to remember these names.")
        print(e)

def cloudSpace():
    print('Which Cooud space wanna use?')
    cSpace = input('Please enter cloud name :: ')
    cloud = {'gdrive' : 'uxrsam','yandex' : 'net.aphos', 'Aux_space' : 'BOX, Deegoo'}
    cName = cloud[cSpace]
    print(cName)




### MAIN PROGRAM ###

# Set up a loop where users can choose what they'd like to do.
names = []

choice = ''
disp__titleBar()
while choice != 'q':

    choice = get_user_choice()

    # Respond to the user's choice.
    disp__titleBar()
    if choice == '1':
        show_names()
    elif choice == '2':
        get_new_name()
    elif choice == '3':
        cloudSpace()
    elif choice == 'q':
        print("\nThanks for playing. Bye.")
    else:
        print("\nI didn't understand that choice.\n")
