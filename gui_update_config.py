#######################################
# 20190609 GUI to update config file
# input.cfg content:
# 		WORK_DIR=/Users/tangpayne/Documents/Coding Learning/Python/20190609
# 		IS_MAC=1
#######################################
from tkinter import *
import re
from button_class import button_class

variable_list = {}

# Open config file to read
config_file = open("input.cfg", "r")
for line in config_file.readlines():
	line = line.rstrip()
	if not re.search("^#", line):
		x = re.split("=", line)
		for element in x:
			exec(x[0] + " = " + "x[1]")
			variable_list[x[0]] = x[1]

config_file.close()

# # Test if variables are read out correctly
# for item in variable_list:
# 	print(item + " = " + variable_list[item])

root = Tk()
left_frame = Frame(root, width=280, height=250, bd=2, relief=SUNKEN)
left_frame.pack(side=LEFT)


for item in variable_list:
 	button_class(item, variable_list[item], left_frame)

root.mainloop()
