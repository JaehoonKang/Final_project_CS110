'''
Analysis:
This logic class implements a counter. The counter is
initially set to zero and is incremented depending on
the function that gets called.
Returns result of test based on how many points the
user incremented throughout.

Process:
Sets counter to zero. Increments by 1, 2, 3, or 4
depending on the function called by the Gui program.
Implements if-elif-else branch to return appropriate
result based on how many points have been incremented.
'''
class PersonalityMaster:
  # Initialize
  def __init__(self):
    # set counter to zero
    self.__value = 0
  # Define function to increment counter by one 
  def increment_one(self):

    self.__value += 1
    print(self.__value)

  # Define function to increment counter by two
  def increment_two(self):

    self.__value += 2
    print(self.__value)

  # Define function to increment counter by three
  def increment_three(self):

    self.__value += 3
    print(self.__value)

  # Define function to increment counter by four
  def increment_four(self):

    self.__value += 4
    print(self.__value)

  # Define function to run point value through if-elif-else
  # branch and return appropriate result
  def result(self):
    if self.__value <= 15:
      result = "You are painfully introverted." +\
               " You shy away from any social situation" +\
               " and try to get through your day making as" +\
               " few waves as possible and you are very duty" +\
               " oriented."
    elif self.__value <= 25:
      result = "You are generally shy, but you don't let" +\
               " that get in the way. You are loyal to your" +\
               " friends and stand up for what's right, even" +\
               " if it means stepping out of your comfort" +\
               " zone."
    elif self.__value <= 30:
      result = "You enjoy high energy social situations" +\
               " and like to have fun. You're very" +\
               " straightforward in your actions and know" +\
               " what you want. You won't let anything slow" +\
               " you down or get in your way."
    else:
      result = "You are a hedonist. You do what you want and" +\
               " you don't let anything get in your way." +\
               " If need be, you will take out those who" +\
               " pose a challenge, and you relish in the fight."
    return result
