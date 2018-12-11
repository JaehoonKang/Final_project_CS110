'''
Analysis: This program prompts the user for a name and provides a
selection of different activities to play.

Input: user name, game choice

Output: Returns user name in choice menu and opens the game of choice

Process: Gets user name from entry box and assigns to variable. Returns
name. Opens game of user's chocie by calling the appropriate function
attached to the button.

'''
#Import
from tkinter import *
import Pers_test as x
import GuessingGUI as y
import CityClass as z



class MainGui:
  #Initialize
  def __init__(self):
    # Create window
    self.__window = Tk()
    # Set title
    self.__window.title("Start")

    #Create frame
    self.__top_frame = Frame(self.__window)
    # Pack frame
    self.__top_frame.pack()

    # Create Label
    self.__Label_1 = Label(self.__top_frame, text = "Welcome. Name: ")
    # Create entry box
    self.__input_name_box = Entry(self.__top_frame)

    # Set Label position
    self.__Label_1.grid(row = 0, column = 0)
    # Set entry box position
    self.__input_name_box.grid(row = 0, column = 1)
    # Bind <Return> key to entry box to call function
    self.__input_name_box.bind("<Return>", self.choose_game)
    # Start listener
    self.__window.mainloop()

  # Define function to open up new window for game choice
  def choose_game(self, event):
    # Get user input from entry box
    name = self.__input_name_box.get()
    #print(name)
    # Destroy old window
    self.__window.destroy()
    # Create new window
    self.__window = Tk()
    # Set title
    self.__window.title("Choose Game")
    # Create Fframe
    self.__topFrame = Frame(self.__window, width = 500, height = 500)
    # Pack frame
    self.__topFrame.pack()
    # Create label
    self.__Label_2 = Label(self.__topFrame, text ="Welcome %s! Choose a game" %(name))
    # Create button 1 to invoke guess game function
    self.__Button_1 = Button(self.__topFrame, text = "Guess", command = self.guess)
    # Create button 2 to invoke personality game function
    self.__Button_2 = Button(self.__topFrame, text = "Personality Test", command = self.pers_test)
    # Create button 3 to invoke cities game function
    self.__Button_3 = Button(self.__topFrame, text = "Cities", command = self.cities)
    # Set position of labels and buttons
    self.__Label_2.grid(row = 1, column = 0)
    self.__Button_1.grid(row = 1, column = 1)
    self.__Button_2.grid(row = 1, column = 2)
    self.__Button_3.grid(row = 1, column = 3)
  # Define function to open personality test Gui and destroy old window
  def pers_test(self):
    self.__window.destroy()
    x.PersTestGui()
  # Define function to open cities Gui and destroy old window
  def cities(self):
    self.__window.destroy()
    z.CityClass()
      
  # Define funtion to open guess Gui and destroy old window
  def guess(self):
    self.__window.destroy()
    y.GuessingGUI()
    
MainGui()





                



