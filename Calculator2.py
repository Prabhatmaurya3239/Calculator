from tkinter import *
import math

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        try:
            value = eval(scvalue.get())
            scvalue.set(value)
        except:
            scvalue.set("Error")
    elif text == "C":
        scvalue.set("")
    elif text == "D":
        scvalue.set(scvalue.get()[:-1])
    elif text == "\u221A":  # Square root
        try:
            scvalue.set(str(math.sqrt(float(scvalue.get()))))
        except:
            scvalue.set("Error")
    elif text == "x²":
        try:
            scvalue.set(str(float(scvalue.get()) ** 2))
        except:
            scvalue.set("Error")
    elif text == "1/x":
        try:
            scvalue.set(str(1 / float(scvalue.get())))
        except:
            scvalue.set("Error")
    elif text == "+/-":
        try:
            scvalue.set(str(-1 * float(scvalue.get())))
        except:
            scvalue.set("Error")
    else:
        scvalue.set(scvalue.get() + text)
    screen.update()

root = Tk()
root.geometry("400x900")
root.title("Advanced Calculator")
root.configure(bg="black")

scvalue = StringVar()
scvalue.set("")

screen = Entry(root, textvar=scvalue, font="Arial 30 bold", bg="white", bd=8, relief=SUNKEN, justify=RIGHT)
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

buttons = [
    ("C", "D", "%", "/"),
    ("7", "8", "9", "*"),
    ("4", "5", "6", "-"),
    ("1", "2", "3", "+"),
    ("00", "0", ".", "="),
    ("\u221A", "x²", "1/x", "+/-"),
]

for row in buttons:
    frame = Frame(root, bg="black")
    for btn in row:
        b = Button(frame, text=btn, padx=20, pady=15, font="Arial 20 bold", bg="gray", fg="white", bd=3, relief=RAISED)
        b.pack(side=LEFT, expand=True, fill=BOTH, padx=5, pady=5)
        b.bind("<Button-1>", click)
    frame.pack(expand=True, fill=BOTH)

root.mainloop()
