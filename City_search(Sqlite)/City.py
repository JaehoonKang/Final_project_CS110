import sqlite3

class City:

    def __init__(self):
        conn = sqlite3.connect('worldDB')
        self.__cursor = conn.cursor()
        self.char = ''

    def get_pop(self, name):
        cityName = name
        self.__cursor.execute("select population from city where name = ?", (cityName,))
        return self.__cursor.fetchone()

    def check_alpha(self, name):
        char = name.split()
        char = ('').join(char)
        ##print(char)
        return char.isalpha()


    def convert_char(self, name):
        for i in name:
            if i != ' ':
                self.char += i
            else:
                i = '_'
                self.char += i
        #print(self.char)
        return self.char

    def reset(self):
        self.char = ''

    def check_lower(self,name):
        name.islower()


def CityTester():
    a = City()

    a.convert_char('xx yy zz')

CityTester()
    

    #def convert_name(self, name):
        



    
