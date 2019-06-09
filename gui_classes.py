#######################################
# 20190609 Classes
#######################################
from tkinter import *

class button_class:
	# Initialize object automatically
	# Master --> root or the main window in GUI
	def __init__(self, master):
		frame = Frame(master)
		frame.pack()

		self.printButton = Button(frame, text="Print message", command=self.print_message)
		self.printButton.pack(side=LEFT)

		self.quitButton = Button(frame, text="Quit", command=frame.quit)
		self.quitButton.pack(side=LEFT)

	def print_message(self):
		print("print_message worked")
		
root = Tk()
b = button_class(root)

# loop the GUI so that it does not close
root.mainloop()
