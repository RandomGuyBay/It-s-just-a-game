from os.path import expanduser
import tkinter as tk
import os
root = tk.Tk()


def play():
    os.startfile("game.pyw")
    exit()
def quit():
    exit()
def eazy():
    file = open("difficulty.txt", "w")
    file.write("2")
    file.close()
def medium():
    file = open("difficulty.txt", "w")
    file.write("1")
    file.close()
def hard():
    file = open("difficulty.txt", "w")
    file.write("0.8")
    file.close()
def back():
    button4.place_forget()
    button5.place_forget()
    button6.place_forget()
    button7.place_forget()
    button1.place(relx=0.375, rely=0.35, relheight=0.05, relwidth=0.25)
    button2.place(relx=0.375, rely=0.4, relheight=0.05, relwidth=0.25)
    button3.place(relx=0.375, rely=0.45, relheight=0.05, relwidth=0.25)
def settings():
    global button4
    global button5
    global button6
    global button7
    button1.place_forget()
    button2.place_forget()
    button3.place_forget()
    button4 = tk.Button(frame, text="Easy", font=("Calibry", 20), command=eazy)
    button4.place(relx=0.375, rely=0.35, relheight=0.05, relwidth=0.25)
    button5 = tk.Button(frame, text="Medium", font=("Calibry", 20), command=medium)
    button5.place(relx=0.375, rely=0.4, relheight=0.05, relwidth=0.25)
    button6 = tk.Button(frame, text="Hard", font=("Calibry", 20), command=hard)
    button6.place(relx=0.375, rely=0.45, relheight=0.05, relwidth=0.25)
    button7 = tk.Button(frame, text="Back", font=("Calibry", 20), command=back)
    button7.place(relx=0.375, rely=0.55, relheight=0.05, relwidth=0.25)
wallpaper = tk.PhotoImage(file='wall.png')
canvas = tk.Canvas(root, width=750, height=50, bg="white", highlightthickness=0)
frame = tk.Frame(root, width=750, height=700, bg="white")
canvas.create_image(0,0, anchor='nw', image=wallpaper)
canvas.create_text(375, 25, text="It is just game", font=("Calibry", 40), fill="white")
canvas.pack()
frame.pack()
button1 = tk.Button(frame, text="Play", font=("Calibry", 20), command=play)
button1.place(relx=0.375, rely=0.35, relheight=0.05, relwidth=0.25)
button2 = tk.Button(frame, text="Settings", font=("Calibry", 20), command=settings)
button2.place(relx=0.375, rely=0.4, relheight=0.05, relwidth=0.25)
button3 = tk.Button(frame, text="Quit", font=("Calibry", 20), command=exit)
button3.place(relx=0.375, rely=0.45, relheight=0.05, relwidth=0.25)
tk.mainloop()