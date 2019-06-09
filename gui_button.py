######################################
# 20190609 GUI Button
######################################
from tkinter import *

root = Tk()
root.geometry("500x500")

def button1_pressed():
	print("Button1 pressed!")

def button2_pressed(event):
	print("Button2 pressed!")

button1 = Button(root, text="Button1", command=button1_pressed)
button1.pack()

button2 = Button(root, text="Button2")
button2.bind("<Button-1>", button2_pressed)
button2.pack()

root.mainloop()

