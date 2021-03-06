from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
from json.decoder import JSONDecodeError


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    search_item = website_entry.get().lower()
    with open(file="data.json", mode="r") as data_file:
        data = json.load(data_file)
        if search_item in data:
            find_email = data[search_item]["email"]
            password = data[search_item]["password"]
            messagebox.showinfo(title=f"{search_item}",  message=f"Email: {find_email}\n Password: {password}\n")
        else:
            messagebox.showerror(title="Error", message="The website does not exist on your database")
       



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def create_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def fetch_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    password_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title=website, message="Email or password cannot be empty")
    else:
        verification = messagebox.askokcancel(title=website,
                                              message=f"Email: {email}\n Password: {password}\n Is it okay to save?")
        if verification:
            try:
                with open("data.json", mode="r") as file:
                    # read file
                    data = json.load(file)
                    # update file
                    data.update(password_data)
            except FileNotFoundError:
                with open("data.json", mode="w") as file:
                    json.dump(password_data, file, indent=4)
            except JSONDecodeError:
                with open("data.json", mode="w") as file:
                    json.dump(password_data, file, indent=4)
            else:
                with open("data.json", mode="w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, "end")
                password_entry.delete(0, "end")
                website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# add labels and position them
website_name = Label(text="Website: ")
website_name.grid(row=1, column=0)
website_entry = Entry(width=25)
website_entry.focus()
website_entry.grid(row=1, column=1)

# Email address
email_name = Label(text="Email/Username: ")
email_name.grid(row=2, column=0)
email_entry = Entry(width=40)
email_entry.insert(0, "fareedatbello1@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

# Search
search_password = Button(text="Search", command=find_password, width=12)
search_password.grid(row=1, column=2)

# Password
password_name = Label(text="Password: ")
password_name.grid(row=3, column=0)
password_entry = Entry(width=22)
password_entry.grid(row=3, column=1)

generate_password = Button(text="Generate Password", command=create_password)
generate_password.grid(row=3, column=2)

add_button = Button(text="Add", width=35, command=fetch_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
