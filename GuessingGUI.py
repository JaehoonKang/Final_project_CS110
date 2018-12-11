'''
Analysis
This program allows the user to guess the right number with the answer

Output to monitor:
The status depending whether the user's answer is right

Input:
    number (int)

Tasks allocated to function:
    get_result()
    

'''
# IMPORT
from tkinter import *
from guessingLogic import *
import Pers_test as x
import CityClass as y

class GuessingGUI:
    # Initialize 
    def __init__(self):

        # create a window on the screen
        self.__window = Tk()
        # set a title 
        self.__window.title("Guessing Game")

        # use a dropdown 
        drop_menu = Menu(self.__window)
        self.__window.config(menu = drop_menu)
        subMenu = Menu(drop_menu)
        drop_menu.add_cascade(label = "More games", menu = subMenu)
        subMenu.add_command(label = "Personality Test", command = self.pers_test)
        subMenu.add_command(label = "Cities", command = self.cities)

        # define a header with StringVar
        self.__header = StringVar() ##########
        # Set the header message
        self.__header.set("Welcome to the Guessing Game")########## 

        # create an instance of the class, guessingLogic
        self.__guessingLogic = guessingLogic()

        
        # create two frame (uppper & lower) 
        self.__upper_frame = Frame(self.__window, width=500, height = 400)
        self.__upper_frame.grid(row=0, column=0)

        self.__lower_frame = Frame(self.__window, width=500, height = 400)
        self.__lower_frame.grid(row=3, column=0)

        # create a label to show the header message
        self.__label_intro = Label(self.__upper_frame, textvariable=self.__header, fg="white", bg="black") ##########
        self.__label_intro.grid(row=0, column =0)

        # create a label to show the program information
        self.__label_intro1 = Label(self.__upper_frame, text="Guess the number between 1 and 99")
        self.__label_intro.grid(row=1, column =0)


        self.__label_right = Label(self.__upper_frame, text="Take a guess below↓↓↓", fg="red", bg="yellow")
        self.__label_right.grid(row=2, column =0)

        # create an entry box to take in the user's input
        self.__entry_guess = Entry(self.__lower_frame)
        self.__entry_guess.grid(row=1, column=0)

        # create a button so when the user hits the button, it invokes a function
        self.__button_input = Button(self.__lower_frame, text="enter", fg="black", bg="white", command=self.get_result)
        self.__button_input.grid(row=1, column=1)

        # Start listener
        self.__window.mainloop()
    # define a function to process the user's input
    def get_result(self): ##########
      # define a variable to store the value that the user inputs in the entrybox
      num = self.__entry_guess.get()

      # Validation: if the input is not an integer
      if not self.__guessingLogic.check_number_int(num):
        self.__header.set("Your number must be an integer")
        #print("pass")
        self.__label_intro.config(fg="yellow", bg="red")

      # if the value passes the validation
      else:
        num = self.__guessingLogic.convert_number(num)
        #print(num)
        # if the number in the input is out of range
        if not self.__guessingLogic.check_range(num):
          res = self.__guessingLogic.get_res()
          #print(res)
          self.__header.set("%s" %res)
          self.__label_intro.config(fg="yellow", bg="red")
        # if the input passes through all the validations
        else:
          #print("passed")
          result = self.__guessingLogic.get_result(num)
          #print(result)

          # this shows the result depending on whether the user's input is right
          if result == "Your guess is smaller than the answer":
              self.__label_intro.config(fg="white", bg="blue")
          elif result == "Your guess is greater than the answer":
              self.__label_intro.config(fg="white", bg="green")
          elif result == "Your guess is exactly right! ★★★★★★":
              self.__label_intro.config(fg="yellow", bg="red")
              self.__button_input.config(state = DISABLED)
              
          self.__header.set("%s" %result)

    # Define function to open of cities game Gui
    def cities(self):
      y.CityClass()

    # Define function to open up personality test Gui
    def pers_test(self):
      x.PersTestGui()
          

#GuessingGUI()
