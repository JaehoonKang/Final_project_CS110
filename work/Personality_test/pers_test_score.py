from tkinter import *
import Pers_test as x

class pers_test_score():
  
  def __init__(self):
    self.__points = 0
    #print(self.__points)

    
  def question_two(self):
    self.__label.config(text = "Question 2")


    #self.__button1 = Button(self.__window)
    self.__button1.config(text = "Hello")
    self.__button1.config(command = self.answer_one)
    #self.__button1.grid(row = 1, column = 0)

    #self.__button2 = Button(self.__window)
    #self.__button2.config(command = self.question_three)
    self.__button2.config(text = "2")
    #self.__button2.grid(row = 2, column = 1)

    #self.__button3 = Button(self.__window)
    self.__button3.config(command = self.question_three)
    #self.__button3.config(command = self.answer_three)
    #self.__button3.grid(row = 3, column = 2)

    #self.__button4 = Button(self.__window)
    #self.__button4.config(command = self.question_three)
    self.__button4.config(command = self.answer_four)
    #self.__button4.grid(row = 4, column = 0)

    self.__button5.config(command = self.question_three)

  def question_three(self):
    self.__label.config(text = "Question 3")


    #self.__button1 = Button(self.__window)
    #self.__button1.config(command = self.question_four)
    self.__button1.config(command = self.answer_one)
    #self.__button1.grid(row = 1, column = 0)

    #self.__button2 = Button(self.__window)
    #self.__button2.config(command = self.question_four)
    self.__button2.config(command = self.answer_two)
    #self.__button2.grid(row = 1, column = 1)

    #self.__button3 = Button(self.__window)
    #self.__button3.config(command = self.question_four)
    self.__button3.config(command = self.answer_three)
    #self.__button3.grid(row = 1, column = 2)

    #self.__button4 = Button(self.__window)
    #self.__button4.config(command = self.question_four)
    self.__button4.config(command = self.answer_four)
    #self.__button4.grid(row = 1, column = 3)

    self.__button5.config(command = self.question_four)

  def question_four(self):
    self.__label.config(text = "Question 4")

  def answer_one(self, event):
    #print('hi')
    self.__points += 1
    print(self.__points)

  def answer_two(self):
    self.__points += 2
    #print(self.__points)


  def answer_three(self):
    self.__points += 3
    #print(self.__points)
    
  def answer_four(self):
    self.__points += 4
    #print(self.__points)



##  def give_personality_type
##    if points <= #:
##      print("")
##    elif points <= ##
##      print("")
##    elif points <= ###
##      print("")
##    else:
##      print("")

