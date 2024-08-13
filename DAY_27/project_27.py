#  Mile to Kilometer converter
from tkinter import *

def miles_to_km():
    miles=float(miles_input.get())
    km=miles*1.609
    kilometer_result_label.config(text=f"{km}")

window=Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20,pady=20)

miles_input=Entry(width=7)
miles_input.grid(column=1,row=0)

miles_label=Label(text="Miles")
miles_label.grid(column=2,row=0)

is_equal_label = Label(text="Is equal to")
is_equal_label.grid(column=0,row=1)

kilometer_result_label=Label(text="KM")
kilometer_result_label.grid(column=2,row=1)

callable_button=Button(text="Calculate",command=miles_to_km)
callable_button.grid(column=1,row=2)




window.mainloop()