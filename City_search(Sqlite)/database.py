import sqlite3
from tkinter import *
import CityData as a

class CityList:
    
    def __init__(self):
        self.__window = Tk()

        conn = sqlite3.connect('worldDB')
        self.__cursor = conn.cursor()
        
        self.__label_intro = Label(self.__window, text= "Welcome to <List of Cities>")
        self.__label_intro.grid(columnspan =3)

        self.__label_des = Label(self.__window, text = "You can explore 10 popular cities. Just click on the name of the city and see the population of the city")
        self.__label_des.grid(columnspan=3)



        self.__button_ny = Button(self.__window, text = "New York")
                                  #command = a.CityData.get_newyork)
        self.__button_ny.bind("<Button-1>", a.CityData.get_newyork)
        self.__button_ny.grid(row=2, column = 0)

        

        self.__button_mc = Button(self.__window, text = "Moscow", command = a.CityData.get_moscow)
        self.__button_mc.grid(row=2, column = 1)

        

        self.__button_me = Button(self.__window, text = "Ciudad_de_México", command = a.CityData.get_mexico)
        self.__button_me.grid(row=2, column = 2)

        
        self.__button_is = Button(self.__window, text = "Istanbul", command = a.CityData.get_istanbul)
        self.__button_is.grid(row=3, column = 0)

       
        self.__button_kr = Button(self.__window, text = "Karachi", command = a.CityData.get_karchi)
        self.__button_kr.grid(row=3, column = 1)

        self.__button_jk = Button(self.__window, text = "Jakarta", command = a.CityData.get_jakarta)
        self.__button_jk.grid(row=3, column = 2)

        self.__button_sh = Button(self.__window, text = "Shanghai", command = a.CityData.get_shanghai)
        self.__button_sh.grid(row=4, column = 0)

        self.__button_sp = Button(self.__window, text = "São_Paulo", command = a.CityData.get_sp)
        self.__button_sp.grid(row=4, column = 1)

        self.__button_kr = Button(self.__window, text = "Seoul", command = a.CityData.get_seoul)
        self.__button_kr.grid(row=4, column = 2)

        self.__button_mb = Button(self.__window, text = "Mumbai", command = a.CityData.get_mumbai)
        self.__button_mb.grid(row=5, column = 1)
        
   

        #self.__cursor.close()

        self.__window.mainloop()
        
    '''
    
    def get_newyork(self):
        root = Tk()
        #root.title = "New York"
        
        #photo = PhotoImage(file="newyork1.gif")
        #label = Label(root, image = photo)
        #label.pack()
        
        
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
        
        #photo = PhotoImage(file="newyork1.gif")
        #label = Label(root, image = photo)
        #label.pack()
        
        
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
        
        #photo = PhotoImage(file="newyork1.gif")
        #label = Label(root, image = photo)
        #label.pack()
        
        
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
        
        #photo = PhotoImage(file="newyork1.gif")
        #label = Label(root, image = photo)
        #label.pack()
        
        
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
        
        #photo = PhotoImage(file="newyork1.gif")
        #label = Label(root, image = photo)
        #label.pack()
        
        
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
        
        #photo = PhotoImage(file="newyork1.gif")
        #label = Label(root, image = photo)
        #label.pack()
        
        
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
        
        #photo = PhotoImage(file="newyork1.gif")
        #label = Label(root, image = photo)
        #label.pack()
        
        
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
        
        #photo = PhotoImage(file="newyork1.gif")
        #label = Label(root, image = photo)
        #label.pack()
        
        
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
        
        #photo = PhotoImage(file="newyork1.gif")
        #label = Label(root, image = photo)
        #label.pack()
        
        
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
        
        #photo = PhotoImage(file="newyork1.gif")
        #label = Label(root, image = photo)
        #label.pack()
        
        
        cityName = "Mumbai"
        self.__cursor.execute("select population from city where name = ?", (cityName,))
        
        result = self.__cursor.fetchone()
        ##print(result)
        
        self.__label_ny_pop = Label(root, text = "Population: %d" %result)
        self.__label_ny_pop.grid(row=0, column=0)
        
        root.mainloop()
    '''

CityList()
#def main():
    #CityList('worldDB')

    #print("Let's find your city and its info")


#main()
    
