######################################
# 20190609 GUI Grid
######################################
from tkinter import *

root = Tk()
root.geometry("500x500")

label1 = Label(root, text="1,1", bg="red", fg="white", font='Avenir 18 bold').grid(row=1)
label2 = Label(root, text="1,2", bg="pink").grid(row=1, column=2)
label3 = Label(root, text="2,3", bg="green").grid(row=2, column=3)
label4 = Label(root, text="3,4", bg="blue").grid(row=3, column=4)
label5 = Label(root, text="1,5", bg="purple").grid(row=1, column=5)
label6 = Label(root, text="column span 2", bg="limegreen").grid(row=2, columnspan=2)
label7 = Label(root, text="label7", bg="lightblue").grid()

root.mainloop()
