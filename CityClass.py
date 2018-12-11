# Import

from tkinter import *
from City import *

"""
Analysis
This program is to find a population of ten cities: New York,
Moscow, Ciudad de México, Istanbul, Karachi, Jakarta, Shanghai,
São_Paulo, Seoul, Mumbai.


Output to monitor:
  population of the city

Input from keyboard:
  name of the city

Tasks allocated to functions:
  show_pop() - when the button is clicked on, this function looks
  for the value
"""    
# Design
# A particular program shows a population of the city that the user looks for

class CityClass:

    def __init__(self):
        # create a window on the screen
        self.__window = Tk()

        # create an instance of the class named City
        self.__data = City()

        # define a header by using StringVar()
        self.__header = StringVar()

        # set the header as the message below
        self.__header.set("Welcome to the Population Guessing Game")

        # create two frames: upper and lower with the size of 300 x 200
        self.__upper_frame = Frame(self.__window, width=300, height = 200)
        self.__upper_frame.grid(row=0, column=0)

        self.__lower_frame = Frame(self.__window, width=300, height = 200)
        self.__lower_frame.grid(row=3, column=0)

        # create label to display the message to the user
        self.__label_intro = Label(self.__upper_frame, \
                                   textvariable=self.__header,\
                                   fg="white", bg="black")

        # using the grid system, set the size of the label
        self.__label_intro.grid(columnspan=3)

        # create a label to show the message below
        self.__label_des = Label(self.__upper_frame, text = \
                                 "You can explore 10 popular\
cities around the world")
        self.__label_des.grid(columnspan=3)

        self.__label_des = Label(self.__upper_frame, text =\
                                 "10 cities: New York, Moscow, \
Ciudad_de_México, Istanbul, Jakarta, Shanghai, São_Paulo, Seoul, Mumbai")
        self.__label_des.grid(columnspan=3)

        self.__label_des = Label(self.__upper_frame, text = \
                                 "Be careful about spellings!:\
New York / Moscow / Istanbul / Jakarta/ Shanghai / Seoul / Mumbai/\
Ciudad_de_México/ São_Paulo")
        self.__label_des.grid(columnspan=3)

        # create a entry box to get the user input
        self.__entry_guess = Entry(self.__upper_frame)
        
        self.__entry_guess.grid(row =4 , column=0)

        # create a button to allow the user to click on the button 
        self.__button_input = Button(self.__upper_frame, text="enter", \
                                     fg="black", bg="white", \
                                     command = self.show_pop)
    
        self.__button_input.grid(row=4, column=1)
   

        self.__window.mainloop()

# Functions ------------------------------------------------------------------

    # when the button is clicked on, this function operates
    # with functions in the backend, this function checks the input and makes
    # relevant message show up on the screen
    def show_pop(self):

        # city_str - the value that the user inputs
        city_str = self.__entry_guess.get()
        
        # if the value is empty
        if city_str == "":

            # it changes the gui on the outside with the warning message
            print('First')
            self.__header.set("You should type in a character")
            self.__label_intro.config(fg="red", bg="yellow")

            # also, empty the value so when the user finds another city,
            # program works fine without an error
            self.__data.reset()
            print("pass")
            
        # if the value is not empty         
        else:

            # check the value is not all string (alphabet)
            if not self.__data.check_alpha(city_str):
                print("second")

                # set the header with a warning meesage
                self.__header.set("You should only type in a valid city name \
(Correct Spellings required, No number or special characters)")
                self.__label_intro.config(fg="red", bg="yellow")
                self.__data.reset()
                print("pass")

            # if the value consists of all string (characters)
            else:

                # convert the value into the right format
                city_strip = self.__data.convert_strip(city_str)
            
                city_lower = self.__data.convert_lower(city_strip)
                ##print(city_lower)

                city_split = self.__data.name_split(city_lower)
                ##print(city_split)

                city_format = self.__data.convert_format(city_split)

                print(city_format)

                # to check the value is not in the city list
                # if the value is not in the city name list
                if not city_format in self.__data.CITY:
                    self.__header.set("Type in a valid city name")
                    self.__label_intro.config(fg="red", bg="yellow")
                # if the value is in the city name list
                else:
                    pop_tp = self.__data.get_pop(city_format)
                
                    pop = pop_tp[0]
                    self.__header.set("Population: %s" %(pop))
                
                self.__data.reset()
                ##print(city_format)
        
            

#CityClass()
