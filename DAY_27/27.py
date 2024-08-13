# 🍵 , Hanji Kaise ho aap sabhi this is 27th day of #100Days_Of_Python I'm back and ready to code.let's start to do code.

# ====================== TKINTER GUI ====================== #

# Tkinter is a default modul use for make graphcal user interface ----> Mac Lisa and cmd is ms-doc

# Creating windows and etc 
import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)

# Label
my_label=tkinter.Label(text="I Am a Label",font=("Arial",24,"bold")) # can do bold,normal,italic
# my_label.pack()
my_label.pack(side="left") # Bottom,expand

# Python Arguments ---> Advance Argument
# Keyword argument --> a,b,c
# argument with default values

# * Unlimited Positional Arguments
# *args --> Many Positional Arguments --> It can take any no of argument , Convert to the tupele

# **kwargs : Many keyword arguments --> Convert to the dict


# Other Components of Tkinter

# Button Entry and Setting components

my_label["text"]="New Text"
my_label.config(text="New Text")

# Button

def button_clicked():
    # print("I get Clicked")
    new_text=input.get()
    my_label.config(text=new_text)
    
def change_text():
    my_label.config(text="Text Changed")

button=tkinter.Button(text="Click Me",command=button_clicked)
# button=tkinter.Button(text="Click Me",command=change_text)
button.pack()

# Entry
# input=tkinter.Entry()
input=tkinter.Entry(width=25)
input.pack()
input.get() # For get inputed values

# Other tkinter Widgets

# * in widgets.py


window.mainloop()