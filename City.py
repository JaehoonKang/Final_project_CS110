# IMPORT
import sqlite3

"""
Analysis
This class works as a logic in the CityClass to find a population of 10 cities
when the user types in a city that they are looking for

This program uses the database system(sqlite3)


Tasks allocated to functions:
  __init__()
  get_pop()
  check_alpha()
  convert_char()
  reset()
  check_lower()
  convert_lower()
  convert_strip()
  name_split()
  convert_format()
  
"""   

class City:
    # CONSTANT
    # this contains all the city names
    CITY = ['New_York', 'Moscow', 'Ciudad_de_México', 'Istanbul', \
            'Karachi', 'Jakarta', 'Shanghai', 'São_Paulo', 'Seoul', 'Mumbai']

    def __init__(self):
        #This program uses the database system(sqlite3)
        conn = sqlite3.connect('worldDB')
        self.__cursor = conn.cursor()
        # create empty string & list
        self.char = ''
        self.li = []
        self.newChar = ''
        
    # using sqlite3 to find the population in the file('WorldDB')
    def get_pop(self, name):
        cityName = name
        self.__cursor.execute("select population from city where name = ?",\
                              (cityName,))
        return self.__cursor.fetchone()
    
    # predicate to check every letter is string
    def check_alpha(self, name):
        #using split method, split the input incase there is two words (e.g. New York)
        char = name.split()
        # using join, combine the splited words
        char = ('').join(char)
        ##print(char)
        return char.isalpha()

    # reset the initialized values
    def reset(self):
        self.char = ''
        self.li = []
        self.newChar = ''
    # predicate to check the word is lowercase
    def check_lower(self,name):
        name.islower()
    # convert the word to a lowercase
    def convert_lower(self, name):
        return name.lower()
    # convert the word to get rid of space on the side
    def convert_strip(self, name):
        return name.strip()
    # splite the word with space
    def name_split(self, name):
        return name.split()

    # convert the value in a right format to use the value in the database
    def convert_format(self, name):

        # if the input is only one word ('Istanbul')
        if len(name) == 1:

            for i in name:
                self.li += i
            # make the first letter in the input capital one
            self.li[0] = self.li[0].upper()
            ##print(self.li)

            for j in self.li:
                self.char += j
        # if the input consists of two words('New York')
        else:
            #print(name)
            # using join method, combine the input with '_'
            y = ('_').join(name)

            #print(y)
            # define a variable, x, to find the index of '_'
            x = y.find('_')
            #print(x)
            for i in name:

                #using title method, make the first letter capital
                self.char += i.title()

            self.char = self.char[0:x] + '_' + self.char[x:]
        #print(self.char)

        return self.char

# predicte to check the input is in the name list
def check_city(self, name):
    if name in CITY:
        return True

        


    
