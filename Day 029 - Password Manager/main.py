from tkinter import *
from tkinter import messagebox
import random
import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
nr_letters = random.randint(8,10)
nr_symbols = random.randint(2,4)
nr_numbers = random.randint(2,4)
 
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    
    pass_letters = [random.choice(letters) for _ in range(nr_letters)]
    pass_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    pass_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    
    password_list = pass_letters + pass_symbols + pass_numbers
    random.shuffle(password_list)
    
    new_password = "".join(password_list)
    password_entry.delete(0,"end")
    password_entry.insert(0, new_password)
    pyperclip.copy(new_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()

    if not website or not email_username or not password:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        return

    new_details = f"{website} | {email_username} | {password}\n"
    
    is_okay = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email_username}\nPassword: {password}"
                           f"\nIs it okay to save?")
    if is_okay:
        with open("data.txt", "a") as data:
            data.write(new_details)
        
        website_entry.delete(0, "end")
        password_entry.delete(0, "end")
        website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file = "logo.png")
canvas.create_image(100,100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)


# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1,row=1, columnspan=2)
website_entry.focus()

email_username_entry = Entry(width=35)
email_username_entry.grid(column=1,row=2, columnspan=2)
email_username_entry.insert(0, "jude@email.com")

password_entry = Entry(width=21)
password_entry.grid(column=1,row=3)

# Buttons
generate_pass_button = Button(text="Generate Password",command=generate_password)
generate_pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()