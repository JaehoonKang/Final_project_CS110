'''
Analysis :
This program determines the type of personality of the user based on
the answers the user gives to the questions.

Input:
Answer choice

Output:
Result of the test (the type of personality of the user).

Process:
Based on the answers the user gives, a point value is incremented
appropriately. Each answer corresponds to a different increment
value. Point count falling within different ranges correspond to
different results.
'''
# IMPORT
from tkinter import *
from PersonalityMaster import *
import GuessingGUI as y
import CityClass as x

class PersTestGui:
  # Initialize
  def __init__(self):

    # Initialize counter to zero
    self.__i = 0

    # Create instance of PesonalityMaster class
    self.__instance = PersonalityMaster()

    # Create Window
    self.__window = Tk()
    
    # Create title
    self.__window.title("Personality Test")
    
    # Set size of window
    self.__window.geometry("1000x200")
    
    # Create drop down menu with options
    drop_menu = Menu(self.__window)
    self.__window.config(menu = drop_menu)
    subMenu = Menu(drop_menu)
    drop_menu.add_cascade(label = "More games", menu = subMenu)
    subMenu.add_command(label = "Guess", command = self.guess)
    subMenu.add_command(label = "Cities", command = self.cities)
    
    
    
    # Configure column
    self.__window.columnconfigure(0, weight = 1)

    # Set StringVar() to question
    self.__question = StringVar()

    # Set first question
    self.__question.set("You're home with your family" +\
                        " and your friends invite you to come out" +\
                        " with them." +\
                        " What do you do?")
    # Create Label
    self.__label = Label(self.__window, textvariable = self.__question)

    # Set column span
    self.__label.grid(columnspan = 3)

    # Create first button with initial answer command
    self.__button1 = Button(self.__window, text = "What friends?",
                            command = self.count_up_one)

    # Set position and span of button
    self.__button1.grid(row = 2, column = 0, sticky = E + W)

    # Create second button with initial answer and command
    self.__button2 = Button(self.__window, text = "It's nice of them to" +\
                          " offer, but I don't get quality" +\
                          " time with my family very often." +\
                          " I'll politely decline.",
                            command = self.count_up_two)

    # Set position and span of button
    self.__button2.grid(row = 3, column = 0, sticky = E + W)

    # Create third button with initial answer command
    self.__button3 = Button(self.__window, text = "Yeah definetely. Sounds fun.",
                            command = self.count_up_three)
    # Set position and span of button
    self.__button3.grid(row = 4, column = 0, sticky = E + W)

    # Create fourth button with initial answer command
    self.__button4 = Button(self.__window, text = "Anything beats" +\
                                                  " being stuck home all day.",
                            command = self.count_up_four)

    # Set position and span of button
    self.__button4.grid(row = 5, column = 0, sticky = E + W)
    
    # Create empty label for space
    self.__empty_label_1 = Label(self.__window, text = "")

    # Set position of label
    self.__empty_label_1.grid(row = 1, column = 0)

    # Create empty label for space
    self.__empty_label_2 = Label(self.__window, text = "")


    # Set position of label
    self.__empty_label_2.grid(row = 6, column = 0)

    # Create fifth button called "Next" with appropriate attributes
    self.__button5 = Button(self.__window, text = "Next", state = DISABLED, command = self.update_question)

    # Set position of button
    self.__button5.grid(row = 7, column = 0)

    # Start listener
    self.__window.mainloop()
  # Define function to increment 1 point and disable answers and enable "Next" button
  def count_up_one(self):
    self.__instance.increment_one()
    self.__button1.config(state = DISABLED)
    self.__button2.config(state = DISABLED)
    self.__button3.config(state = DISABLED)
    self.__button4.config(state = DISABLED)
    self.__button5.config(state = NORMAL)
  # Define function to increment 2 points and disable answers and enable "Next" button
  def count_up_two(self):
    self.__instance.increment_two()
    self.__button1.config(state = DISABLED)
    self.__button2.config(state = DISABLED)
    self.__button3.config(state = DISABLED)
    self.__button4.config(state = DISABLED)
    self.__button5.config(state = NORMAL)
  # Define function to increment 3 points and disable answers and enable "Next" button
  def count_up_three(self):
    self.__instance.increment_three()
    self.__button1.config(state = DISABLED)
    self.__button2.config(state = DISABLED)
    self.__button3.config(state = DISABLED)
    self.__button4.config(state = DISABLED)
    self.__button5.config(state = NORMAL)
  # Define function to increment 4 points and disable answers and enable "Next" button
  def count_up_four(self):
    self.__instance.increment_four()
    self.__button1.config(state = DISABLED)
    self.__button2.config(state = DISABLED)
    self.__button3.config(state = DISABLED)
    self.__button4.config(state = DISABLED)
    self.__button5.config(state = NORMAL)
  # Define function to reset question and answers, restore buttons' original
  # states, and print out result if there are no more questions
  def update_question(self):
    QUESTIONS = ["You just finish a difficult final" +\
                 " and someone suggests you all go" +\
                 " out to eat. What do you do?",
                 "You're walking along and you see ahead of you" +\
                 " an old acquaintance. What do you do?",
                 "You're walking along and all of a sudden" +\
                 " you bump into the most beautiful person you've" +\
                 " ever seen. What do you do?",
                 "How do you spend a typical Saturday afternoon?",
                 "You're on your way somewhere and you see a" +\
                 " stray cat on the side of the road. It looks" +\
                 " hurt and very weak. What do you do?",
                 "400.72 + 511 + 1006.89",
                 "You decide to start working out because...?",
                 "You overhear some people behind you talking" +\
                 " badly about someone you know. Suddenly they" +\
                 " turn to you and ask you what you think." +\
                 " You're not a fan of this person either. Well...?",
                 "You're minding you're own business when suddenly" +\
                 " some guy walks up to you and yells, 'What the" +\
                 " hell is your problem!?' How do you react?"]
    ANSWERS = [["*Walk away before anyone sees you*",
                "Hmmm. Well I'll go if my friends go.",
                "Nice! So where are we going?",
                "You got that right! Everyone in my car!" +\
                " We're gonna have some fun!"],
               ["*Look down and keep walking." +\
                " Hopefully they don't see me*",
                "*Brighten up* Oh look who it is." +\
                " Maybe I'll go say hi.",
                "Hi! How have you been? I've missed you.",
                "Hey! Remember me? HEY! Get back here!"],
               ["S-Sorry. *Walk away*",
                "Wow! You're so beautiful.",
                "Exuse me. Do you want to go out with me sometime?",
                "I’m no mathematician, but I’m pretty good with" +\
                " numbers. Tell you what, give me yours and watch" +\
                " what I can do with it."],
               ["study, study study",
                "study, youtube, study",
                "study, youtube, youtube",
                "youtube, youtube, youtube"],
               ["Awww. Kitty come here. I won't hurt you. *I need" +\
                " to get him to an animal hospital*",
                "You poor thing. Come here. I'll take you home and get you" +\
                " all better.",
                "Oh man. That cat looks like it's in bad shape. I hope it gets" +\
                "better soon. *Walks away*",
                "Who did this to you! Tell me! I swear I'm gonna make them" +\
                " pay!"],
               ["*Fully focused on finding the answer*",
                "*Takes out a paper and pencil*",
                "*Takes out a calculator*",
                "*Does something else*"],
               ["It's important to take care of your body. Also, it's" +\
                " everyone's responsibility to be physically capable" +\
                " of handling themselves. Getting stronger will" +\
                " help me accomplish that.",
                "I'd like to get stronger. And I guess I wouldn't mind" +\
                " looking a little better.",
                "I want to look good.",
                "Can't get girls without killing those curls."],
               ["*Shrug shoulders and look away*",
                "You guys really shouldn't speak badly about people" +\
                " behind their backs. It's immoral.",
                "I don't have any problems with them",
                "Yeah I agree. He/she is pretty annoying."],
               ["Ignore them and continue doing what you were doing.",
                "What do you mean? I've never even seen you before?",
                "I don't know what you're talking about but" +\
                " if you take one step closer I'm gonna lay you out.",
                "I don't know what's going on here but I like it!" +\
                " Let's fight!"]]
    if self.__i < len(QUESTIONS):
      
      #print(self.__i)
      self.__question.set(QUESTIONS[self.__i])
      self.__button1.config(text = ANSWERS[self.__i][0])
      self.__button2.config(text = ANSWERS[self.__i][1])
      self.__button3.config(text = ANSWERS[self.__i][2])
      self.__button4.config(text = ANSWERS[self.__i][3])

      self.__button1.config(state = NORMAL)
      self.__button2.config(state = NORMAL)
      self.__button3.config(state = NORMAL)
      self.__button4.config(state = NORMAL)
      self.__button5.config(state = DISABLED)

      self.__i += 1
      
    else:
      self.__button1.destroy()
      self.__button2.destroy()
      self.__button3.destroy()
      self.__button4.destroy()
      self.__button5.destroy()
      print(self.__instance.result())
      self.__question.set(self.__instance.result())
      #print("Result")

  # Define function to open up guessing game Gui
  def guess(self):
    y.GuessingGUI()

  # Define function to open up cities game Gui
  def cities(self):
    x.CityClass()
    
    
#PersTestGui()


