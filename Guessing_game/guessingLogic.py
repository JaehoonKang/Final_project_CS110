import random


class guessingGame:

    def __init__(self):
        self.answer = random.randint(1,99)

    def is_number(self, num):
        return num.isdigit()

    def is_greater(self, num):
        #print("what the hell")
        if 0 < int(num) or 100 > int(num):
            return True
