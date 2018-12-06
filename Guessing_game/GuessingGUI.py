from tkinter import *

class GuessingGUI:

    def __init__(self):
        self.__window = Tk()

        self.__upper_frame = Frame(self.__window, width=500, height = 400)
        self.__upper_frame.grid(row=0, column=0)

        self.__lower_frame = Frame(self.__window, width=500, height = 400)
        self.__lower_frame.grid(row=3, column=0)

        self.__label_intro = Label(self.__upper_frame, text="Welcome to the Guessing Game")
        self.__label_intro.grid(row=0, column =0)

        self.__label_intro = Label(self.__upper_frame, text="Guess the number between 1 and 99")
        self.__label_intro.grid(row=1, column =0)


        self.__label_right = Label(self.__upper_frame, text="Take a guess below↓↓↓", fg="red", bg="yellow")
        self.__label_right.grid(row=2, column =0)

        self.__entry_guess = Entry(self.__lower_frame)
        #self.__entry_guess.config(command=compare_value)
        self.__entry_guess.grid(row=1, column=0)


        self.__button_input = Button(self.__lower_frame, text="enter", fg="white", bg="black")
        #command=self.get_value)
        self.__button_input.grid(row=1, column=1)

        self.__window.mainloop()

GuessingGUI()