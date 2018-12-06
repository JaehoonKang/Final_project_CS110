from  guessingLogic import *

def guessingLogicTester():

    this_game = guessingGame()

    print(this_game.answer)
    
    user_str = input("What is your gueess?")

    while user_str:

        while not this_game.is_number(user_str):
            print("Your number is not an integer")
            print("Please enter a valid number between 0 and 100")

            user_str = input("What is your guess?:  ")

        while not this_game.is_greater(user_str):

            print("Your number is not in the range")

            user_str = input("What is your guess?:  ")

        user = int(user_str)


        if user > this_game.answer:

            print("bigger")

        elif user < this_game.answer:

            print("smaller")

        else:

            print("You are right!")


        user_str = input("What is your guess?:  ")

guessingLogicTester()
