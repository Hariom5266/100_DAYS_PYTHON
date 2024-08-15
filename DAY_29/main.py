from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters=[choice(letters) for _ in range(randint(8, 10))]
    password_symbols=[choice(symbols) for _ in range(randint(2, 4))]
    password_numbers=[choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters+password_symbols+password_numbers
    shuffle(password_list)

    password="".join(password_list)
    # print(f"Your password is: {password}")
    
    if len(password_entry.get()) > 0:
        password_entry.delete(0,END)
    password_entry.insert(0,password)
    pyperclip.copy(password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_data=website_entry.get()
    email_data=email_entry.get()
    password_data=password_entry.get()
    
    if len(website_data)==0 or len(password_data)==0:
        messagebox.showinfo(title="Oops",message="Please make sure you haven't left any field empty.")
    else:    
        is_ok=messagebox.askokcancel(title="Save",message=f"These are entered details: \nEmail: {email_data}\nPassword: {password_data}\nIs it ok to save?")
        
        if is_ok:    
            with open("./DAY_29/data.txt",mode='a') as file:
                file.write(f"{website_data} | {email_data} | {password_data}\n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)
            website_entry.focus()
    
# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(width=200,height=200)
logo=PhotoImage(file="./DAY_29/logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(row=0,column=1)

# Labels
website_label=Label(text="Website/App: ")
website_label.grid(row=1,column=0)
email_label=Label(text="Email/Username: ")
email_label.grid(row=2,column=0)
password_label=Label(text="Password: ")
password_label.grid(row=3,column=0)

# Entries
website_entry=Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2,pady=7)
website_entry.focus()
email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2,pady=7)
email_entry.insert(0,"abc@gmail.com")
password_entry=Entry(width=35)
password_entry.grid(row=3,column=1,pady=7)

# Buttons
generate_password_btn=Button(text="Generate Password",highlightthickness=0,command=generate_password)
generate_password_btn.grid(row=3,column=5,pady=7)
add_button=Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2,pady=7)

window.mainloop()