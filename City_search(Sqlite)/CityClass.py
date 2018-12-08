from tkinter import *
from City import *


class CityClass:

    def __init__(self):
        self.__window = Tk()

        self.__data = City()

        self.__header = StringVar() ##########
        self.__header.set("Welcome to the Population Guessing Game")##########

        #conn = sqlite3.connect('worldDB')
        #self.__cursor = conn.cursor()

        self.__upper_frame = Frame(self.__window, width=300, height = 200)
        self.__upper_frame.grid(row=0, column=0)

        self.__lower_frame = Frame(self.__window, width=300, height = 200)
        self.__lower_frame.grid(row=3, column=0)
        
        self.__label_intro = Label(self.__upper_frame, textvariable=self.__header, fg="white", bg="black") ##########
        self.__label_intro.grid(columnspan=3)
        
        self.__label_des = Label(self.__upper_frame, text = "You can explore 10 popular cities around the world")
        self.__label_des.grid(columnspan=3)

        self.__label_des = Label(self.__upper_frame, text = "10 cities: New York, Moscow, Ciudad_de_México, Istanbul, Jakarta,\
Shanghai, São_Paulo, Seoul, Mumbai")
        self.__label_des.grid(columnspan=3)

        self.__label_des = Label(self.__upper_frame, text = "Be careful about spellings!: New York / Moscow / Istanbul / Jakarta/ \
Shanghai / Seoul / Mumbai/ Ciudad_de_México/ São_Paulo")
        self.__label_des.grid(columnspan=3)
             
        self.__entry_guess = Entry(self.__upper_frame)
        #self.__entry_guess.config(command=compare_value)
        self.__entry_guess.grid(row =4 , column=0)

        self.__button_input = Button(self.__upper_frame, text="enter", fg="black", bg="white", command = self.show_pop)
    
        self.__button_input.grid(row=4, column=1)
   

        #self.__cursor.close()

        self.__window.mainloop()

    def show_pop(self):

        city_str = self.__entry_guess.get()

        

        '''
        if city_str == "":
            print('First')
            self.__header.set("You should type in a character")
            self.__label_intro.config(fg="red", bg="yellow")
            self.__data.reset()
            print("pass")
            
        else:
            if not self.__data.check_alpha(city_str):
                print("second")
                self.__header.set("You should only type in a valid city name \
(Correct Spellings required, No number or special characters)")
                self.__label_intro.config(fg="red", bg="yellow")
                self.__data.reset()
                print("pass")
            else:
                print("third")
                city = self.__data.convert_char(city_str)
                #print(city)
                pop_tp = self.__data.get_pop(city)
                pop = pop_tp[0]
                self.__header.set("Population of %s: %s" %(city_str, pop))
                self.__data.reset()
            '''

CityClass()
