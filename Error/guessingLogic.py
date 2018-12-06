import random

answer = random.randint(1,99)

print(answer)

class guessingGame:

    def __init__(self):
        self.answer = random.randint(1,99)

    def is_number(self, num):
        return num.isdigit()

    def is_greater(self, num):
        if 0 < num and 100 > num:
            return True


def guessingLogicTester():

    this_game = guessingGame()


    user_str = input("What is your gueess?")
    
    while user_str:
        
        while not this_game.is_number(user_str) and this_game.is_greater(user_str):
            print("Your number is not an integer")
            print("Please enter a valid number between 0 and 100")
        
            user_str = input("What is your guess?")


        user = int(user_str)


        if user > this_game.answer:

            print("bigger")

        elif user < answer:

            print("smaller")

        else:

            print("You are right!")


        user_str = input("What is your guess")

#guessingLogicTester()
