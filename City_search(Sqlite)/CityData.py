import sqlite3
from tkinter import *

class CityData:
    def __init__(self):
        print("hello")

    def get_newyork(self, event):
        root = Tk()
        #root.title = "New York"
        '''
        photo = PhotoImage(file="newyork1.gif")
        label = Label(root, image = photo)
        label.pack()
        '''
        
        cityName = "New_York"
        self.__cursor.execute("select population from city where name = ?", (cityName,))
        
        result = self.__cursor.fetchone()
        ##print(result)
        
        self.__label_ny_pop = Label(root, text = "Population: %d" %result)
        self.__label_ny_pop.grid(row=0, column=0)
        
        root.mainloop()

    def get_moscow(self):
        root = Tk()
        #root.title = "Moscow"
        '''
        photo = PhotoImage(file="newyork1.gif")
        label = Label(root, image = photo)
        label.pack()
        '''
        
        cityName = "Moscow"
        self.__cursor.execute("select population from city where name = ?", (cityName,))
        
        result = self.__cursor.fetchone()
        ##print(result)
        
        self.__label_ny_pop = Label(root, text = "Population: %d" %result)
        self.__label_ny_pop.grid(row=0, column=0)
        
        root.mainloop()

    def get_mexico(self):
        root = Tk()
        #root.title = "Moscow"
        '''
        photo = PhotoImage(file="newyork1.gif")
        label = Label(root, image = photo)
        label.pack()
        '''
        
        cityName = "Ciudad_de_México"
        self.__cursor.execute("select population from city where name = ?", (cityName,))
        
        result = self.__cursor.fetchone()
        ##print(result)
        
        self.__label_ny_pop = Label(root, text = "Population: %d" %result)
        self.__label_ny_pop.grid(row=0, column=0)
        
        root.mainloop()

    def get_istanbul(self):
        root = Tk()
        #root.title = "Moscow"
        '''
        photo = PhotoImage(file="newyork1.gif")
        label = Label(root, image = photo)
        label.pack()
        '''
        
        cityName = "Istanbul"
        self.__cursor.execute("select population from city where name = ?", (cityName,))
        
        result = self.__cursor.fetchone()
        ##print(result)
        
        self.__label_ny_pop = Label(root, text = "Population: %d" %result)
        self.__label_ny_pop.grid(row=0, column=0)
        
        root.mainloop()

    def get_karchi(self):
        root = Tk()
        #root.title = "Moscow"
        '''
        photo = PhotoImage(file="newyork1.gif")
        label = Label(root, image = photo)
        label.pack()
        '''
        
        cityName = "Istanbul"
        self.__cursor.execute("select population from city where name = ?", (cityName,))
        
        result = self.__cursor.fetchone()
        ##print(result)
        
        self.__label_ny_pop = Label(root, text = "Population: %d" %result)
        self.__label_ny_pop.grid(row=0, column=0)
        
        root.mainloop()

    def get_jakarta(self):
        root = Tk()
        #root.title = "Moscow"
        '''
        photo = PhotoImage(file="newyork1.gif")
        label = Label(root, image = photo)
        label.pack()
        '''
        
        cityName = "Jakarta"
        self.__cursor.execute("select population from city where name = ?", (cityName,))
        
        result = self.__cursor.fetchone()
        ##print(result)
        
        self.__label_ny_pop = Label(root, text = "Population: %d" %result)
        self.__label_ny_pop.grid(row=0, column=0)
        
        root.mainloop()

    def get_shanghai(self):
        root = Tk()
        #root.title = "Moscow"
        '''
        photo = PhotoImage(file="newyork1.gif")
        label = Label(root, image = photo)
        label.pack()
        '''
        
        cityName = "Shanghai"
        self.__cursor.execute("select population from city where name = ?", (cityName,))
        
        result = self.__cursor.fetchone()
        ##print(result)
        
        self.__label_ny_pop = Label(root, text = "Population: %d" %result)
        self.__label_ny_pop.grid(row=0, column=0)
        
        root.mainloop()

    def get_sp(self):
        root = Tk()
        #root.title = "Moscow"
        '''
        photo = PhotoImage(file="newyork1.gif")
        label = Label(root, image = photo)
        label.pack()
        '''
        
        cityName = "São_Paulo"
        self.__cursor.execute("select population from city where name = ?", (cityName,))
        
        result = self.__cursor.fetchone()
        ##print(result)
        
        self.__label_ny_pop = Label(root, text = "Population: %d" %result)
        self.__label_ny_pop.grid(row=0, column=0)
        
        root.mainloop()

    def get_seoul(self):
        root = Tk()
        #root.title = "Moscow"
        '''
        photo = PhotoImage(file="newyork1.gif")
        label = Label(root, image = photo)
        label.pack()
        '''
        
        cityName = "Seoul"
        self.__cursor.execute("select population from city where name = ?", (cityName,))
        
        result = self.__cursor.fetchone()
        ##print(result)
        
        self.__label_ny_pop = Label(root, text = "Population: %d" %result)
        self.__label_ny_pop.grid(row=0, column=0)
        
        root.mainloop()

    def get_mumbai(self):
        root = Tk()
        #root.title = "Moscow"
        '''
        photo = PhotoImage(file="newyork1.gif")
        label = Label(root, image = photo)
        label.pack()
        '''
        
        cityName = "Mumbai"
        self.__cursor.execute("select population from city where name = ?", (cityName,))
        
        result = self.__cursor.fetchone()
        ##print(result)
        
        self.__label_ny_pop = Label(root, text = "Population: %d" %result)
        self.__label_ny_pop.grid(row=0, column=0)
        
        root.mainloop()
        
