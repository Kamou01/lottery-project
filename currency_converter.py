from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import requests
from playsound import playsound

gui = Tk()
gui.title("Currency Converter")
gui.geometry("600x600")
gui.config(bg="green")
# playsound('')


def convert_curency():
    get_rates = "https://v6.exchangerate-api.com/v6/21d57e3e0d14d58eee61f22c/latest/" + cb1.get()
    rates = requests.get(get_rates).json()
    rates = float(e1.get()) * rates["conversion_rates"][cb2.get()]
    messagebox.showinfo("answer", rates)
    if "ok":
        import claim


def clear_button():
    e1.delete(0, END)
    cb2.delete(0, END)
    cb2.delete(0, END)


l1 = Label(gui, text="Enter your amount: ", font="Arial 12", fg="white", bg="green")
l1.place(x=250, y=20)
e1 = Entry(gui, width=15)
e1.place(x=250, y=50)



# label
l3 = Label(gui, text="Choose your currency: ", font="Arial 12", fg="white", bg="green")
l3.place(x=190, y=100)
cb1 = Combobox(gui, width=15)
cb1.place(x=250, y=130)

cb1["values"] = ("ZAR",
                 "USD",
                 "EUR",
                 "AUD",
                 "GBP",
                 "CAD",
                 "JPY")


l2 = Label(gui, text="Choose the currency you want to convert to:", font="Arial 12", fg="white", bg="green")
l2.place(x=170, y=190)
cb2 = Combobox(gui, width=15)
cb2.place(x=250, y=220)

cb2["values"] = ("ZAR",
                 "USD",
                 "EUR",
                 "AUD",
                 "GBP",
                 "CAD",
                 "JPY")


convrt_btn = Button(gui, text="Convert", font="Arial 12", fg="white", bg="green", command=convert_curency)
convrt_btn.place(x=250, y=300)

clr_btn = Button(gui, text="Clear", font="Arial 12", fg="white", bg="green", command=clear_button)
clr_btn.place(x=350, y=300)

# display window
d1_display = Label(gui, font="Arial 15")
d1_display.place(x=170, y=350, width=300, height=200)

# running the window
gui.mainloop()
