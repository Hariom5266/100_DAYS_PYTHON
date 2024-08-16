from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
import json

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
    website_data = website_entry.get()
    email_data = email_entry.get()
    password_data = password_entry.get()

    # Ensure website_data is a valid key and not empty
    if len(website_data) == 0 or len(password_data) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any field empty.")
        return

    new_data = {
        website_data: {
            "email": email_data,
            "password": password_data
        }
    }
    
    is_ok = messagebox.askokcancel(
        title="Save", 
        message=f"These are the entered details: \nEmail: {email_data}\nPassword: {password_data}\nIs it ok to save?"
    )
    
    if is_ok:
        try:
            # Try to open the file and read existing data
            with open("./DAY_30/data.json", 'r') as file:
                # Read the existing file content
                file_content = file.read().strip()
                if file_content:
                    data = json.loads(file_content)  # Load JSON data if file is not empty
                else:
                    data = {}  # Initialize as empty if the file is empty
        except (FileNotFoundError, json.JSONDecodeError):
            # If file doesn't exist or is invalid, start with empty data
            data = {}   
        
        # Update data with new_data
        data.update(new_data)
        
        # Write the updated data back to the file
        with open("./DAY_30/data.json", 'w') as file:
            json.dump(data, file, indent=4)
        
        # Clear the entry fields after saving
        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    data={}
    website=website_entry.get()
    try:
        with open("./DAY_30/data.json","r") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror("Oops!",message="Data file can't found")
    except json.JSONDecodeError:
        messagebox.showerror("Error!",message="No Data in File.")
    
    else:
        # Searching in json 
        if website in data:
            email=data[website]["email"]
            password=data[website]["password"]
            messagebox.showinfo(title="Search Succesful",message=f"Website: {website}\nEmail: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Search Unsuccesful",message=f"{website} is not found.")
            
# ---------------------------- UI SETUP ------------------------------- #
# Create the main window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg='#f7f7f7')

# Add logo
canvas = Canvas(window, width=200, height=200, bg='#f7f7f7', highlightthickness=0)
logo = PhotoImage(file="./DAY_29/logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1, columnspan=3, pady=(0, 20))

# Styling
label_font = ('Segoe UI', 12)
entry_font = ('Segoe UI', 12)
button_font = ('Segoe UI', 10, 'bold')

# Colors
label_color = '#333333'
entry_bg_color = '#ffffff'
button_bg_color = '#0078d4'  # A modern blue color
button_fg_color = '#ffffff'
button_hover_bg_color = '#005a9e'  # A darker blue for hover effect

# Labels
website_label = Label(window, text="Website/App:", font=label_font, bg='#f7f7f7', fg=label_color)
website_label.grid(row=1, column=0, sticky='e', padx=(0, 10))
email_label = Label(window, text="Email/Username:", font=label_font, bg='#f7f7f7', fg=label_color)
email_label.grid(row=2, column=0, sticky='e', padx=(0, 10))
password_label = Label(window, text="Password:", font=label_font, bg='#f7f7f7', fg=label_color)
password_label.grid(row=3, column=0, sticky='e', padx=(0, 10))

# Entries
website_entry = Entry(window, width=35, font=entry_font, bg=entry_bg_color)
website_entry.grid(row=1, column=1, columnspan=2, padx=(0, 10))
website_entry.focus()

email_entry = Entry(window, width=35, font=entry_font, bg=entry_bg_color)
email_entry.grid(row=2, column=1, columnspan=2, padx=(0, 10))
email_entry.insert(0, "abc@gmail.com")

password_entry = Entry(window, width=35, font=entry_font, bg=entry_bg_color)
password_entry.grid(row=3, column=1, columnspan=2, padx=(0, 10))

# Buttons
def on_enter(e):
    e.widget['background'] = button_hover_bg_color

def on_leave(e):
    e.widget['background'] = button_bg_color

search_button = Button(window, text="Search", width=13, font=button_font, command=find_password, bg=button_bg_color, fg=button_fg_color)
search_button.grid(row=1, column=3, padx=(10, 0))
search_button.bind("<Enter>", on_enter)
search_button.bind("<Leave>", on_leave)

generate_password_btn = Button(window, text="Generate Password", font=button_font, command=generate_password, bg=button_bg_color, fg=button_fg_color)
generate_password_btn.grid(row=3, column=3, padx=(10, 0))
generate_password_btn.bind("<Enter>", on_enter)
generate_password_btn.bind("<Leave>", on_leave)

add_button = Button(window, text="Add", width=36, font=button_font, command=save, bg=button_bg_color, fg=button_fg_color)
add_button.grid(row=4, column=1, columnspan=3, pady=(20, 0))
add_button.bind("<Enter>", on_enter)
add_button.bind("<Leave>", on_leave)

window.mainloop()


