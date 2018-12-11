from tkinter import *
import Pers_test as x
#import Guess as y
#from rpg_final_project import *
#import rpg_final_project as s
def main():
  mainGui()


  mainloop()
class mainGui():
  def __init__(self):
    self.__window = Tk()

    self.__topFrame = Frame(self.__window)# width = 500, height = 500)
    self.__topFrame.pack()

    self.__botFrame = Frame(self.__window) #width = 500, height = 500)
    self.__botFrame.pack()


    self.__Label_1 = Label(self.__topFrame, text = "Welcome. Name: ")
    self.__input_name_box = Entry(self.__topFrame)
    #name = self.__input_name_box.get()
    #print(name)
    self.__Label_1.grid(row = 0, column = 0)
    self.__input_name_box.grid(row = 0, column = 1)

    self.__input_name_box.bind("<Return>", self.choose_game)
    
  def choose_game(self, event):
    name = self.__input_name_box.get()
    #print(name)
    self.__window.destroy()
    self.__window = Tk()
    self.__topFrame = Frame(self.__window, width = 500, height = 500)
    self.__topFrame.pack()
    self.__Label_2 = Label(self.__topFrame, text ="Welcome %s! Choose a game" %(name))
    self.__Button_1 = Button(self.__topFrame, text = "Numbers", command = self.guess)
    self.__Button_2 = Button(self.__topFrame, text = "Personality Test", command = self.pers_test)
    self.__Label_2.grid(row = 1, column = 0)
    self.__Button_1.grid(row = 1, column = 1)
    self.__Button_2.grid(row = 1, column = 2)

  def pers_test(self):
    #self.persTestGui()
    self.__window.destroy()
    x.PersTestGui()

  def guess(self):
    self.__window.destroy()
    y.GuessingGame()
    
    



main()


                



