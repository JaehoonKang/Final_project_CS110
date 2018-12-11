class PersonalityMaster:
  
  def __init__(self):

    self.__value = 0

  def increment_one(self):

    self.__value += 1
    print(self.__value)

  def increment_two(self):

    self.__value += 2
    print(self.__value)
    
  def increment_three(self):

    self.__value += 3
    print(self.__value)

  def increment_four(self):

    self.__value += 4
    print(self.__value)

  def result(self):
    if self.__value <= 15:
      result = "Result 1"
    elif self.__value <= 25:
      result = "Result 2"
    elif self.__value <= 30:
      result = "Result 3"
    else:
      result = "Result 4"
    return result
