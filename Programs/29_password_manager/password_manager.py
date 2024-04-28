import tkinter as tk
from tkinter import messagebox
from password_generator import password_generator
import json

# Color palette
LIGHT_PINK = "#FFE6E6"
PINK = "#E1AFD1"
LAVENDER = "#AD88C6"
VIOLET = "#7469B6"

# Adding to json file 
def add_entry():
    website_val = website_store.get()
    email_val = email_store.get()
    password_val = password_store.get()
    if website_val == '' or email_val == '' or password_val == '' :
            messagebox.showinfo(parent=window, message= 'Error: A field is left empty.')
    else:
        to_store = {website_val: {
                        "email" : email_val,
                        "password" : password_val
                        }} 
        try:
            with open("saved_passwords.json", "r") as file:
                try:
                    data = json.load(file)
                except json.decoder.JSONDecodeError:
                    data = {}
        except FileNotFoundError:
            open("saved_passwords.json", "w").close()
            data ={}
        finally:
            if website_val in data:
                new = messagebox.askokcancel(parent=window, message = f"Details for {website_val} already exist. Would you like to replace with \nEmail: {email_val} \nPassword: {password_val}?")
                if new:
                    data[website_val]['email'] = email_val
                    data[website_val]['password'] = password_val
            else:
                ok = messagebox.askokcancel(parent=window, message = f" Is this ok?\nWebsite: {website_val} \nEmail: {email_val} \nPassword: {password_val}")
                if ok:  
                    data.update(to_store)
            with open("saved_passwords.json", "w") as file:
                json.dump(data, file, indent=4)
            website_store.delete(0, tk.END)
            email_store.delete(0, tk.END)
            password_store.delete(0, tk.END)
            messagebox.showinfo(parent=window, message = 'Password successfully saved!')

def generate_pass():
    password_store.delete(0, tk.END)
    new_pass = password_generator()
    password_store.insert(0, new_pass)

# Search function for already existing website
def search_website():
    website_val = website_store.get()
    try:
        with open("saved_passwords.json", "r") as file:
            data = json.load(file)
        messagebox.showinfo(parent=window, message= f"The details for {website_val} are:\n Email: {data[website_val]['email']}\n Password: {data[website_val]['password']}")
    except KeyError:
        messagebox.showinfo(parent=window, message = f"Password for {website_val} doesn't exist. Please add details first.")
    except FileNotFoundError:
        messagebox.showinfo(parent=window, message = "File doesn't exist, please create a file first.")
        
window = tk.Tk()
window.title("Lock and Key Password Manager")
window.configure(bg=LIGHT_PINK, padx= 30, pady= 30)
window.geometry("550x500")

# Canvas Image
canvas = tk.Canvas(window, width = 273, height = 236, highlightthickness=0)
logo = tk.PhotoImage(file = "lock_and_key.png")
canvas.create_image(136, 118, image = logo)
canvas.grid(row = 1, column = 1, columnspan=2)

# Website label and entry box
website = tk.Label(text = "Website:", bg=LIGHT_PINK, fg=LAVENDER, font = ("Arial", 14))
website.grid(row = 2, column = 1, padx= 4)

website_store = tk.Entry(cursor='arrow')
website_store.configure(width = 20, font=('Arial', 14),  bg = PINK, fg = VIOLET, highlightthickness=0)
website_store.grid(row = 2, column = 2, padx = 10, pady = 5, sticky="w")

## Search button
search_button=tk.Button(text = 'Search', font = ("Arial", 14), width=15, fg = LAVENDER, height = 2, highlightthickness=0, borderwidth= 0, command =search_website)
search_button.grid(row = 2, column = 2, padx = 10, pady = 5, sticky="e")

# Email / Username label and entry box
email = tk.Label(text = "Email / Username:", bg=LIGHT_PINK, fg=LAVENDER, font = ("Arial", 14))
email.grid(row = 3, column = 1, padx= 4)

email_store = tk.Entry(cursor='arrow')
email_store.configure(width = 40, font=('Arial', 14),  bg = PINK, fg = VIOLET, highlightthickness=0)
email_store.grid(row = 3, column = 2, padx = 10, pady = 5)


# Password label and entry box 
password = tk.Label(text = "Password:", bg=LIGHT_PINK, fg=LAVENDER, font = ("Arial", 14))
password.grid(row = 4, column = 1, padx= 4)

password_store = tk.Entry(cursor='arrow')
password_store.configure(width = 20, font=('Arial', 14),  bg = PINK, fg = VIOLET, highlightthickness=0)
password_store.grid(row = 4, column = 2, sticky="w", padx = 10, pady = 5)

# Generate password button 
gen_pass=tk.Button(text = 'Generate Password', font = ("Arial", 14), width=15, fg = LAVENDER, height = 2, highlightthickness=0, borderwidth= 0, command = generate_pass)
gen_pass.grid(row = 4, column = 2, padx = 10, pady = 5, sticky="e")

# Add button to add password to text file
add_pass=tk.Button(text = 'Add', font = ("Arial", 14), width=37, fg = LAVENDER, height = 2, highlightthickness=0, borderwidth=0, command= add_entry)
add_pass.grid(row = 5, column = 2, columnspan= 2, padx = 10, pady = 5)

website_store.focus_force()

window.mainloop()