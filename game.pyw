import tkinter as tk
import random as rn
import threading as td
import time
import os
if os.path.exists("difficulty.txt"):
    file = open("difficulty.txt")
    difficulty = file.read()
    file.close()
else:
    file = open("difficulty.txt", "w")
    file.write("2")
    file.close()
    difficulty = 2
root = tk.Tk()
root.geometry("+0+0")
e = tk.Entry(root, width=0, borderwidth=0)
e.place(relx=1)
e.insert(tk.INSERT, "0")
def go_menu():
    os.startfile("menu.pyw")
    exit()
if bool(os.path.exists("coins.txt")):
    file = open("coins.txt")
    money = file.read()
    if money == "":
        file.close()
        file = open("coins.txt", "w")
        file.write("0")
        file.close()
else:
    file = open("coins.txt", "w")
    file.write("0")
    file.close()
wallpaper = tk.PhotoImage(file='wall.png')
def add_bod(test="ne"):
    x = e.get()
    xx = int(x)
    if xx == 10:
        file = open("coins.txt")
        money = file.read()
        file.close()
        file = open("coins.txt", "w")
        file.write(f"{int(money) + 1}")
    xx = int(x)
    if xx == 100:
        file = open("coins.txt")
        money = file.read()
        file.close()
        file = open("coins.txt", "w")
        file.write(f"{int(money) + 10}")
    xx = int(x)
    if xx == 1000:
        file = open("coins.txt")
        money = file.read()
        file.close()
        file = open("coins.txt", "w")
        file.write(f"{int(money) + 100}")
    if test == "yes":
        x = e.get()
        e.delete("0", tk.END)
        e.insert(tk.INSERT, f"{int(x)+ 3}")
        #canvas.create_rectangle(0, 0, 750, 50, fill="white", outline="white")
        canvas.create_image(0,0, anchor='nw', image=wallpaper)
        canvas.create_text(600, 25, text=f"Score: {x}", font=("Calibry", 40), fill="white")
    else:
        x = e.get()
        e.delete("0", tk.END)
        e.insert(tk.INSERT, f"{int(x) - 2}")
        #canvas.create_rectangle(0, 0, 750, 50, fill="white", outline="white")
        canvas.create_image(0,0, anchor='nw', image=wallpaper)
        canvas.create_text(600, 25, text=f"Score: {x}", font=("Calibry", 40), fill="white")
def random_stvorec():
    global difficulty
    difficulty
    try:
        frame = tk.Frame(root, width=750, height=700, bg="#5885AF")
        frame.pack()
        test = "yes"
        while True:
            add_bod()
            """farba = "#"
            for i in range(6):
                farba += rn.choice("ABCDEF0123456789")"""
            farba = "#43B0F1"
            x = rn.random()
            y = rn.random()
            if x >= 0.95:
                x = 0.95
            if y >= 0.95:
                y = 0.95
            button = tk.Button(frame, bg=farba, activebackground=farba, command=lambda: add_bod(test), bd=0)
            button.place(relx=x, rely=y, relwidth=0.05, relheight=0.055)
            time.sleep(float(difficulty))
            button.place_forget()
    except RuntimeError:
        print("Neviem ale error ale to je jedno")
canvas = tk.Canvas(root, width=750, height=50, bg="white", highlightthickness=0)
thread_1 = td.Thread(target=random_stvorec)
thread_1.start()
canvas.pack()
canvas.create_image(0,0, anchor='nw', image=wallpaper)
menu = tk.Button(canvas, text="Main menu", font=("Calibry", 25), command=lambda: go_menu(), bg="#274472", fg="white", activebackground="#000C66", activeforeground="white")
menu.place(relx=0, rely=0, relwidth=0.25, relheight=1)
tk.mainloop()