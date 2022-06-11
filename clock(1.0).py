from tkinter import Tk
from tkinter import Label
import time
import sys
from datetime import date

master = Tk()
master.title("CLOCK")
master.configure(bg="Black")

def get_date():
    datevar = date.today()
    date1.config(text=datevar)
    date1.after(200,get_date)

def get_time():
    timeVar = time.strftime("%I:%M:%S %p")
    clock.config(text=timeVar)
    clock.after(200,get_time)


clock = Label(master, font=("Arial",100),bg="black",fg="white")
clock.pack()
date1 = Label(master, font=("Arial",50),fg="white",bg="black")
date1.pack()

get_date()
get_time()
print(date1)

master.mainloop()
