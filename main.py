from tkinter import *
from time import *

def update():
    time_string=strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string=strftime("%A")
    day_label.config(text=day_string)

    date_string=strftime("%d/%B/%Y")
    date_label.config(text=date_string)

    window.after(1000,update) #After 1000ms(1 second), call update again

window = Tk()

time_label = Label(window,
                   font=("Arial", 50),
                   fg="#00FF00",
                   bg="#000000")
time_label.pack(fill="both", expand=True)

day_label = Label(window,
                   font=("Arial", 30),
                  fg="#00FF00",
                  bg="#000000",)
day_label.pack(fill="both", expand=True)

date_label = Label(window,
                   font=("Arial", 40),
                  fg="#00FF00",
                  bg="#000000",)
date_label.pack(fill="both", expand=True)

update()

window.mainloop()