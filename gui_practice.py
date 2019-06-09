######################################
# 20190609 GUI practice
######################################
from tkinter import *

# Functions
def update_text(event):
	text_var.set(mid_entry.get())
	mid_entry.delete(0, END) # Clear the entry field

# Top
root = Tk()
# root.geometry("100x500")

# Fix window size
root.minsize(width=280, height=200)
root.maxsize(width=280, height=200)

top_frame = Frame(root, width=500, height=50, bd=2, relief=FLAT)
top_frame.pack()

# Prevent frame to shrink its size to fit content
top_frame.pack_propagate(0)

top_label = Label(top_frame, text="Python GUI practice: Update Label text")
top_label.pack()

# Middle
mid_frame = Frame(root, width=280, height=25, bd=2, relief=SUNKEN)
mid_frame.pack()
mid_frame.pack_propagate(0)

text_var = StringVar()
mid_label = Label(mid_frame, textvariable=text_var, anchor=W, justify=LEFT).pack(fill=X)
text_var.set("xxx")

# Entry
mid_entry = Entry(root, width=280)
mid_entry.pack()

mid_button = Button(root, text="Update")
mid_button.pack()
mid_button.bind("<Button-1>", update_text)

root.mainloop()
