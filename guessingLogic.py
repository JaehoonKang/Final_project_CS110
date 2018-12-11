'''
Analysis
This program works as a logic for the class, GuessingGUI
and allows the user to chooose the city and
shows the population of the city

Output to monitor:
The population of the city 

Input:
    cityname (str)

Tasks allocated to function:
    greater_hundred()
    smaller_zero()
    smaller_zero(0
    is_greater()
    is_smaller()
    is_equal()
    check_number_int()
    get_result()
'''

# IMPORT
import random


class guessingLogic:
    #initialize
    def __init__(self):

        #define the answer
        self.__answer = random.randint(1,99) ##########
        print(self.__answer) ##########
        self.__result = ""
    # predicate to check the value is greater than 100
    def greater_hundred(self, num):
        #print(num)
        return 100 < int(num)
    # predicate to check the value is smaller than 0
    def smaller_zero(self, num):
        #print(num)
        return 0 > int(num)
    # predicate to check whether the value is greater than the answer
    def is_greater(self, num):
        return self.__answer < num
    # predicate to check whether the value is smaller than the answer
    def is_smaller(self, num):
        return self.__answer > num
    # predicate to check whether the value is equal to the answer
    def is_equal(self, num):
        return self.__answer == num
    # predicate 
    def check_number_int(self, num): ##########
      return num.isdigit()
    # convert the value to an integer
    def convert_number(self, num): ##########
      return int(num)

    # this shows the status depending on
    # whether the input is right/ greater/ smaller
    def get_result(self, num): ##########
        
      if num < self.__answer:
        self.__result = "Your guess is smaller than the answer"
          
      elif num > self.__answer:
        self.__result = "Your guess is greater than the answer"

      else:
        self.__result = "Your guess is exactly right! ★★★★★★"
        
      return self.__result

    # this checks if the value is out of range
    def check_range(self,num):
      if  num >= 100:
            self.__result = "Your number should be less than 100"
###        set_fg()
      elif num <= 0:
            self.__result = "Your number should be greater than 0"
      return (num < 100) and (num > 0)
    # to get the result
    def get_res(self):
        return self.__result
    
###    def set_fg(self):
###      fg = yellow
###      return fg
      
