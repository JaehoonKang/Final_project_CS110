import random


class guessingLogic:

    def __init__(self):
        self.answer = random.randint(1,99)

    #def is_number(self, num):
        #return num.isdigit()

    def greater_hundred(self, num):
        #print("what the hell")
        return 100 < int(num)

    def smaller_zero(self, num):
        #print("what the hell")
        return 0 > int(num)

    def is_greater(self, num):
        return self.answer < num

    def is_smaller(self, num):
        return self.answer > num

    def is_equal(self, num):
        return self.answer == num
