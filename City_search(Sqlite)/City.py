import sqlite3

class City:

    def __init__(self):
        conn = sqlite3.connect('worldDB')
        self.__cursor = conn.cursor()
        self.char = ''
        self.li = []
        self.newChar = ''

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
        self.li = []
        self.newChar = ''

    def check_lower(self,name):
        name.islower()

    def convert_lower(self, name):
        return name.lower()

    def convert_strip(self, name):
        return name.strip()

    def name_split(self, name):
        return name.split()

    

    def convert_format(self, name):

        if len(name) == 1:

            for i in name:
                self.li += i
            self.li[0] = self.li[0].upper()
            ##print(self.li)

            for j in self.li:
                self.char += j

        else:
            #print(name) 
            
            y = ('_').join(name)

            #print(y)
            
            x = y.find('_')

            #print(x)

            
            for i in name:
                self.char += i.title()

            

            self.char = self.char[0:x] + '_' + self.char[x:]
        #print(self.char)

        return self.char
                

    

'''        
def CityTester():
    a = City()

    a.convert_char('xx yy zz')

CityTester()
    

    #def convert_name(self, name):
        

'''

    
