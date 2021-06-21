from tkinter import *
from tkinter import messagebox
import random
from playsound import playsound

gui = Tk()
gui.geometry("700x900")
gui.title("Let's Play")
gui.config(bg="green")

img = PhotoImage(file="image1.png")
Label(gui, image=img, width=312, height=167).place(x=200, y=5)


def play_game():
    usernum1 = int(sb1.get())
    usernum2 = int(sb2.get())
    usernum3 = int(sb3.get())
    usernum4 = int(sb4.get())
    usernum5 = int(sb5.get())
    usernum6 = int(sb6.get())
    user_numbers = {usernum1, usernum2, usernum3, usernum4, usernum5, usernum6}

    x = random.sample(range(1, 49), 6)
    set(x)

    clr_numbers()

    userent1 = x[0]
    userent2 = x[1]
    userent3 = x[2]
    userent4 = x[3]
    userent5 = x[4]
    userent6 = x[5]

    e1.insert(0, x[0])
    e2.insert(0, x[1])
    e3.insert(0, x[2])
    e4.insert(0, x[3])
    e5.insert(0, x[4])
    e6.insert(0, x[5])
    user_entries = {userent1, userent2, userent3, userent4, userent5, userent6}

    comp = set(user_numbers).intersection(set(user_entries))
    print(user_entries)
    print(user_numbers)
    print(len(comp))
    print(comp)

    if len(comp) == 1:
        f = open('login.txt', 'w')
        f.write("Numbers entered: " + str(user_entries) + ", ")
        f.write("Winning numbers: " + str(user_entries) + ", ")
        f.close()
        messagebox.showinfo("Congratulations, but: ", "You matched 1 number, 1 number = R0.00")
    elif len(comp) == 2:
        f = open('login.txt', 'w')
        f.write("Numbers entered: " + str(user_entries) + ", ")
        f.write("Winning numbers: " + str(user_entries) + ", ")
        f.close()
        messagebox.showinfo("Congratulations", "You matched 2 numbers, 2 numbers = R20.00")
        import claim
    elif len(comp) == 3:
        f = open('login.txt', 'w')
        f.write("Numbers entered: " + str(user_entries) + ", ")
        f.write("Winning numbers: " + str(user_entries) + ", ")
        f.close()
        messagebox.showinfo("Congratulations", "You matched 3 numbers, 3 numbers = R100.50")
        import claim
    elif len(comp) == 4:
        f = open('login.txt', 'w')
        f.write("Numbers entered: " + str(user_entries) + ", ")
        f.write("Winning numbers: " + str(user_entries) + ", ")
        f.close()
        messagebox.showinfo("Congratulations", "You matched 4 numbers, 4 numbers = R2,384.00")
        import claim
    elif len(comp) == 5:
        f = open('login.txt', 'w')
        f.write("Numbers entered: " + str(user_entries) + ", ")
        f.write("Winning numbers: " + str(user_entries) + ", ")
        f.close()
        messagebox.showinfo("Congratulations", "You matched 5 numbers, 5 numbers = R8,584.00")
        import claim
    elif len(comp) == 6:
        f = open('login.txt', 'w')
        f.write("Numbers entered: " + str(user_entries) + ", ")
        f.write("Winning numbers: " + str(user_entries) + ", ")
        f.close()
        messagebox.showinfo("Congratulations", "You matched 6 numbers, 6 numbers = R10,000 000.00")
        import claim
    else:
        messagebox.showinfo("Sorry", "You have not matched any numbers, that's tough son ")


def clr_numbers():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)

    sb1.delete(0, END)
    sb2.delete(0, END)
    sb3.delete(0, END)
    sb4.delete(0, END)
    sb5.delete(0, END)
    sb6.delete(0, END)


def play_again():
    clr_numbers()


def how_to_play():
    message = messagebox.showinfo("Confused?", "In order to play, you need to choose numbers from 1-49, and hope for the best. Goodluck!!!")


def exit_button():
    gui.destroy()


sb1 = Spinbox(gui, from_=1, to=49, width=4, font="Arial 12", bg="red")
sb1.place(x=160, y=200)

sb2 = Spinbox(gui, from_=1, to=49, width=4, font="Arial 12", bg="purple")
sb2.place(x=230, y=200)

sb3 = Spinbox(gui, from_=1, to=49, width=4, font="Arial 12", bg="green")
sb3.place(x=300, y=200)

sb4 = Spinbox(gui, from_=1, to=49, width=4, font="Arial 12", bg="blue")
sb4.place(x=370, y=200)

sb5 = Spinbox(gui, from_=1, to=49, width=4, font="Arial 12", bg="orange")
sb5.place(x=440, y=200)

sb6 = Spinbox(gui, from_=1, to=49, width=4, font="Arial 12", bg="yellow")
sb6.place(x=510, y=200)

play_btn = Button(gui, text="Play", font="Arial 15", command=play_game, fg="white", bg="green")
play_btn.place(x=200, y=280)

clr_btn = Button(gui, text="Clear", font="Arial 15", command=clr_numbers, fg="white", bg="green")
clr_btn.place(x=400, y=280)

e1 = Entry(gui, state="normal", width=5, font="Arial 12")
e1.place(x=160, y=350)

e2 = Entry(gui, state="normal", width=5, font="Arial 12")
e2.place(x=230, y=350)

e3 = Entry(gui, state="normal", width=5, font="Arial 12")
e3.place(x=300, y=350)

e4 = Entry(gui, state="normal", width=5, font="Arial 12")
e4.place(x=370, y=350)

e5 = Entry(gui, state="normal", width=5, font="Arial 12")
e5.place(x=440, y=350)

e6 = Entry(gui, state="normal", width=5, font="Arial 12")
e6.place(x=510, y=350)

d1_display = Label(gui, font="Arial 15")
d1_display.place(x=190, y=430, width=350, height=300)


ply_btn = Button(gui, text="Play Again", font="Arial 15", fg="white", bg="green", command=play_again)
ply_btn.place(x=150, y=750)

ext_btn = Button(gui, text="Exit", font="Arial 15", fg="white", bg="green", command=exit_button)
ext_btn.place(x=200, y=800)

prz_lb1 = Label(gui, text="winning numbers: '6': R10, 000, 000.00", font="Arial 10")
prz_lb1.place(x=200, y=450)

prz_lb2 = Label(gui, text="winning numbers: '5': R8,584.00", font="Arial 10")
prz_lb2.place(x=200, y=500)

prz_lb3 = Label(gui, text="winning numbers: '4': R2,384.00", font="Arial 10")
prz_lb3.place(x=200, y=550)

prz_lb4 = Label(gui, text="winning numbers: '3': R100.50", font="Arial 10")
prz_lb4.place(x=200, y=600)

prz_lb5 = Label(gui, text="winning numbers: '2': R20.00", font="Arial 10")
prz_lb5.place(x=200, y=650)

prz_lb6 = Label(gui, text="winning numbers: '1': R0", font="Arial 10")
prz_lb6.place(x=200, y=700)


cnfsn_btn = Button(gui, text="Confused?", font="Arial 15", fg="white", bg="green", command=how_to_play)
cnfsn_btn.place(x=450, y=800)

# running the window
gui.mainloop()
