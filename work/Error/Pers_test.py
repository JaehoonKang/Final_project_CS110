from tkinter import *
#import pers_test_score as a
#from PersonalityMaster import PersonalityMaster
from PersonalityMaster import *

class PersTestGui:
  
  def __init__(self):
    
    self.__i = 0

    self.__instance = PersonalityMaster()

    
    self.__window = Tk()

    self.__label = Label(self.__window, text = "You're home with your family" +\
                         " and your friends invite you to come out with them." +\
                         " What do you do?")
    self.__label.grid(columnspan = 3)


    self.__button1 = Button(self.__window, text = "What friends?")
                            #command = self.count_up_one)
    self.__button1.bind("<Button-1>", self.count_up_one)
    self.__button1.grid(row = 1, column = 0)

    self.__button2 = Button(self.__window, text = "It's nice of them to" +\
                          " offer, but I don't get quality" +\
                          " time with my family very often." +\
                          " I'll politely decline.",
                            command = self.count_up_two)

    #self.__button2.config(command = a.pers_test_score.answer_two)
    self.__button2.grid(row = 2, column = 0)

    self.__button3 = Button(self.__window, text = "",
                            command = self.count_up_three)

    self.__button3.grid(row = 3, column = 0)

    self.__button4 = Button(self.__window, text = "",
                            command = self.count_up_four)
    
    self.__button4.grid(row = 4, column = 0)

    self.__next_label = Label(self.__window, text = "")
    self.__next_label.grid(row = 5, column = 0)

    self.__button5 = Button(self.__window, text = "Next", command = self.update_question)
    self.__button5.grid(row = 6, column = 0)

    #a.pers_test_score()
    
    self.__window.mainloop()

  def count_up_one(self,event):
    self.__instance.increment_one()

  def count_up_two(self):
    self.__PersonalityMaster.increment_two()

  def count_up_three(self):
    self.__PersonalityMaster.increment_three()

  def count_up_four(self):
    self.__PersonalityMaster.increment_four()

  def update_question(self):
    QUESTIONS = ["Q1", "Q2", "Q3"]
    ANSWERS = [["A1", "A2", "A3", "A4"],
               ["A12", "A22", "A32", "A42"]]
    if self.__i < len(QUESTIONS)-1:
      self.__i += 1
      self.__label["text"] = QUESTIONS[self.__i]
      self.__button1["text"] = ANSWERS[self.__i-1][0]
      self.__button2["text"] = ANSWERS[self.__i-1][1]
      self.__button3["text"] = ANSWERS[self.__i-1][2]
      self.__button4["text"] = ANSWERS[self.__i-1][3]
      
    else:
      self.__button1.destroy()
      self.__button2.destroy()
      self.__button3.destroy()
      self.__button4.destroy()
      self.__button5.destroy()
      self.__label.destroy()
      #self.__label["text"] = self.__PersonalityMaster.result()
      #print("Result")
    
    
PersTestGui()


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
    



