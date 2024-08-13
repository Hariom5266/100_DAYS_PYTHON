# Tkinter Layout Manager

# * pack
# Pack --> default start from center of the screen
# adding side parameter can change in any side
# Problem is not can see at precise place

# * Place
# Can give x and y value

# * Grid
# Entire program realize as a grid
# grid(column=0,row=0)
# It is relative
# cant make grid and place not can use both in one program

from tkinter import *

Window=Tk()
Window.minsize(height=500,width=500)



new_button=Button(text="New Button")
new_button.grid(column=2,row=0)











Window.mainloop()