#######################################
# 20190609 Classes 2
#######################################
from tkinter import *

array = (
  "Button1",
  "Button2",
  "Button3"
)

class button_class:
	def __init__(self, button_name, master):
		self.name = button_name

		frame = Frame(master)
		frame.pack(side=TOP)

		self.clickButton = Button(frame, text=button_name, command=self.button_clicked)
		self.clickButton.pack(side=LEFT)

		self.quitButton = Button(frame, text="Quit", command=frame.quit)
		self.quitButton.pack(side=LEFT)

	def button_clicked(self):
		print(self.name + " clicked!")

root = Tk()
for element in array:
	button_class(element, root)

root.mainloop()
