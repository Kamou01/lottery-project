from tkinter import *
from playsound import playsound

gui = Tk()
gui.geometry("700x700")
gui.title("Do you wanna be rich?")
gui.config(bg="green")
# playsound("theme.mp3")

# functions
#play button


def entry_btn():
    gui.destroy()
    import login

# exit button


def exit_btn():
    gui.destroy()


# image
img = PhotoImage(file="image1.png")
Label(gui, image=img, width=312, height=167).place(x=200, y=5)

# label - heading
l1 = Label(gui, text="Do you wanna be a millionaire?", fg="white", bg="green", font="Arial 15")
l1.place(x=200, y=200)

# Enter button
entry_btn = Button(gui, text="Let's play", fg="white", bg="green", command=entry_btn, font="Arial 12")
entry_btn.place(x=220, y=300)


# exit button
exit_btn = Button(gui, text="Exit", fg="white", bg="green", font="Arial 12", command=exit_btn)
exit_btn.place(x=400, y=300)

# running the window
gui.mainloop()
