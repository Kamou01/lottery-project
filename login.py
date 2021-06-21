from tkinter import *
from tkinter import messagebox
import rsaidnumber
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
import random
from playsound import playsound

gui = Tk()
gui.geometry("700x700")
gui.title("Login")
gui.config(bg="green")

img = PhotoImage(file="image1.png")
Label(gui, image=img, width=312, height=167).place(x=200, y=5)


def exit_program():
    message = messagebox.askquestion("", "You sure you want to exit?")
    if message == "yes":
        gui.destroy()
        import main
    else:
        print("go back")


def verify_program():
    player_id = rsaidnumber.parse(e3.get())
    print(player_id)
    birthday = player_id.date_of_birth
    player_age = relativedelta(date.today(), birthday.date())
    print(player_age.years)

    x = random.sample(range(1, 49), 2)
    set(x)

    if player_age.years >= 18:
        f = open('login.txt', 'w')
        f.write("Name: " + e1.get() + ", ")
        f.write("Email: " + e2.get() + ", ")
        f.write("Id no: " + e3.get() + ", ")
        f.close()
        # playsound('Effect.mp3')
        messagebox.showinfo("Congratulations", "You are eligible to play")
        messagebox.showinfo("", "Welcome player_" + str(x[0]) + str(x[1]))
        gui.destroy()
        import lottery

    elif player_age.years < 18:
        messagebox.showinfo("You are too young to play")
    else:
        pass


# except ValueError:
# playsound('Gandalf.mp3')
# messagebox.showerror("Error", "Invaid Id no")


l1 = Label(gui, text="Enter your Username: ", fg="white", bg="green", font="Arial 12")
l1.place(x=10, y=200)
e2 = Entry(gui, state="normal", width=30)
e2.place(x=300, y=300)

l2 = Label(gui, text="Enter your Email Address: ", fg="white", bg="green", font="Arial 12")
l2.place(x=10, y=300)
e1 = Entry(gui, state="normal", width=30)
e1.place(x=300, y=200)

l3 = Label(gui, text="Enter your I.D number : ", fg="white", bg="green", font="Arial 12")
l3.place(x=10, y=400)

e3 = Entry(gui, state="normal", width=30)
e3.place(x=300, y=400)

verify_btn = Button(gui, text="Verify", fg="white", bg="green", font="Arial 12", command=verify_program)
verify_btn.place(x=300, y=600)

exit_btn = Button(gui, text="Exit", fg="white", bg="green", font="Arial 12", command=exit_program)
exit_btn.place(x=500, y=600)

# running the window
gui.mainloop()
