######################################
# 20190609 GUI Label
######################################
from tkinter import *

root = Tk()
root.geometry("500x500")

label1 = Label(root, text="label1", bg="red", fg="white", font='Avenir 18 bold').pack(fill=X)
label2 = Label(root, text="label2", bg="pink").pack(side=LEFT)
label3 = Label(root, text="label3", bg="green").pack(side=RIGHT)
label4 = Label(root, text="label4", bg="blue").pack(side="left")
label5 = Label(root, text="label5", bg="purple").pack(side="right")
label6 = Label(root, text="label6", bg="limegreen").pack(side=BOTTOM)
label7 = Label(root, text="label7", bg="lightblue").pack()

root.mainloop()
