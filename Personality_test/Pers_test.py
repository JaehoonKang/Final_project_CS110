from tkinter import *
import pers_test_score as a

class PersTestGui():
  
  def __init__(self):
    self.__window = Tk()

    self.__label = Label(self.__window, text = "You're home with your family" +\
                         " and your friends invite you to come out with them." +\
                         " What do you do?")
    self.__label.grid(columnspan = 3)

    print(a.pers_test_score.answer_one)
    self.__button1 = Button(self.__window, text = "What friends?")
                            #command = a.pers_test_score.answer_one)
    self.__button1.bind("<Button-1>",a.pers_test_score.answer_one)
    self.__button1.grid(row = 1, column = 0)

    self.__button2 = Button(self.__window, text = "It's nice of them to" +\
                          " offer, but I don't get quality" +\
                          " time with my family very often." +\
                          " I'll politely decline.", command = a.pers_test_score.answer_two)

    self.__button2.config(command = a.pers_test_score.answer_two)
    self.__button2.grid(row = 2, column = 0)

    self.__button3 = Button(self.__window)

    self.__button3.config(command = a.pers_test_score.answer_three)
    self.__button3.grid(row = 3, column = 0)

    self.__button4 = Button(self.__window)
    
    self.__button4.config(command = a.pers_test_score.answer_four)
    self.__button4.grid(row = 4, column = 0)

    self.__next_label = Label(self.__window, text = "")
    self.__next_label.grid(row = 5, column = 0)

    self.__button5 = Button(self.__window, text = "Next", command = a.pers_test_score.question_two)
    self.__button5.grid(row = 6, column = 0)

    a.pers_test_score()
    
    self.__window.mainloop()


##  def question_two(self):
##    #print("Hi")
##    self.__label.config(text = "Question 2")
##
##
##    #self.__button1 = Button(self.__window)
##    self.__button1.config(text = "Hello")
##    self.__button1.config(command = self.answer_one)
##    #self.__button1.grid(row = 1, column = 0)
##
##    #self.__button2 = Button(self.__window)
##    #self.__button2.config(command = self.question_three)
##    self.__button2.config(text = "2")
##    #self.__button2.grid(row = 2, column = 1)
##
##    #self.__button3 = Button(self.__window)
##    self.__button3.config(command = self.question_three)
##    #self.__button3.config(command = self.answer_three)
##    #self.__button3.grid(row = 3, column = 2)
##
##    #self.__button4 = Button(self.__window)
##    #self.__button4.config(command = self.question_three)
##    self.__button4.config(command = self.answer_four)
##    #self.__button4.grid(row = 4, column = 0)
##
##    self.__button5.config(command = self.question_three)
##
##  def question_three(self):
##    self.__label.config(text = "Question 3")
##
##
##    #self.__button1 = Button(self.__window)
##    #self.__button1.config(command = self.question_four)
##    self.__button1.config(command = self.answer_one)
##    #self.__button1.grid(row = 1, column = 0)
##
##    #self.__button2 = Button(self.__window)
##    #self.__button2.config(command = self.question_four)
##    self.__button2.config(command = self.answer_two)
##    #self.__button2.grid(row = 1, column = 1)
##
##    #self.__button3 = Button(self.__window)
##    #self.__button3.config(command = self.question_four)
##    self.__button3.config(command = self.answer_three)
##    #self.__button3.grid(row = 1, column = 2)
##
##    #self.__button4 = Button(self.__window)
##    #self.__button4.config(command = self.question_four)
##    self.__button4.config(command = self.answer_four)
##    #self.__button4.grid(row = 1, column = 3)
##
##    self.__button5.config(command = self.question_four)
##
##  def question_four(self):
##    self.__label.config(text = "Question 4")
##
##
##    
##
##
##
##  def answer_one(self):
##    global points
##    points += 1
##    print(points)
##
##  def answer_two(self):
##    global points
##    points += 2
##    print(points)
##
##
##  def answer_three(self):
##    global points
##    points += 3
##    print(points)
##    
##  def answer_four(self):
##    global points
##    points += 4
##    print(points)
##
####  def give_personality_type
####    if points <= #:
####      print("")
####    elif points <= ##
####      print("")
####    elif points <= ###
####      print("")
####    else:
####      print("")
    



