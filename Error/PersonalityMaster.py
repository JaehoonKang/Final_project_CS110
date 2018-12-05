class PersonalityMaster:
  
  def __init__(self):

    self.__value = 0

  def increment_one(self):

    self.__value += 1

  def increment_two(self):

    self.__value += 2
    
  def increment_three(self):

    self.__value += 3

  def increment_four(self):

    self.__value += 4

  def result(self):
    if self.__value <= 15:
      print("Result 1")
    elif self.__value <= 25:
      print("Result 2")
    elif self.__value <= 30:
      print("Result 3")
    else:
      print("Result 4")
    return result
      

    
      
