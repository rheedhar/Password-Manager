from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


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

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title=website, message="Email or password cannot be empty")
    else:
        verification = messagebox.askokcancel(title=website, message=f"Email: {email}\n Password: {password}\n Is it okay to save?" )
        if verification:
            with open("password.txt", mode="a") as file:
                file.write(f"{website} | {email} | {password}\n")
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
website_entry = Entry(width=40)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

# Email address
email_name = Label(text="Email/Username: ")
email_name.grid(row=2, column=0)
email_entry = Entry(width=40)
email_entry.insert(0, "fareedatbello1@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

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
