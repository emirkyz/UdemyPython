import tkinter as tk
from tkinter import messagebox
from password_generator import generate_psswrd
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
reps = False
def generate():
    global reps
    if reps:
        password_entry.delete(0,tk.END)
    reps = True
    password = generate_psswrd()
    password_entry.insert(tk.END,password)
    print(reps)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(password)==0 or len(website)==0:
        messagebox.showerror(title="Error", message="Don't leave password and website fields empty")
    else:
        is_ok = messagebox.askokcancel(title = website, message=f"These are the details entered \nEmail: {email} \nPassword: {password}\nIs it okay to save")

    if is_ok:
        with open("data.txt","a") as data_file:
            data_file.write(f"{website} / {email} / {password}\n")
            website_entry.delete(0,tk.END)
            password_entry.delete(0,tk.END)
            email_entry.delete(0,tk.END)

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)


canvas = tk.Canvas(height=200,width=200)
logo_image = tk.PhotoImage(file = "logo.png")
canvas.create_image(100, 100 ,image = logo_image)
canvas.grid(row = 0, column = 1)


#Labels
website_label = tk.Label(text="Website:")
website_label.grid(row=1,column=0)
email_label = tk.Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = tk.Label(text = "Password:")
password_label.grid(row = 3, column = 0)


#Entry
website_entry = tk.Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()

email_entry = tk.Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)



password_entry = tk.Entry(width=21)
password_entry.grid(row=3,column=1)


#Buttons
generate_password_button = tk.Button(text="Generate password",command=generate)
generate_password_button.grid(column=2,row=3)


add_button = tk.Button(text="Add",width=36,command=save_password)
add_button.grid(row=4,column=1,columnspan=2)




window.mainloop()