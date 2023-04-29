import tkinter as tk

window= tk.Tk()


window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=30, pady=30)

# Label
my_label = tk.Label(text="I am a label" , font=("Arial", 24, "bold"))
my_label.grid(column=0,row=0) ## bu olmadan gözükmez

my_label["text"] = "New Text"
my_label.config(text="New Text",padx=10,pady=10)

#button

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button = tk.Button(text="Click me", command=button_clicked)
# button.place(x = 0, y = 100)
button.grid(column=1, row=1) # grid ve pack aynı anda kullanılmaz



# Entry

input = tk.Entry(width=24)
input.insert(string= "test" , index=0)
input.grid(column=2, row=2)
print(input.get())


# pack place and grid








# text = tk.Text(height=6, width=30)
# text.focus()
# text.insert("1.0", "Example of multi-line text entry.")
# text.pack()
#
#
# # Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))
#
# listbox = tk.Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>",listbox_used)
# listbox.pack()
# listbox.mainloop()
#
# listbox.pack()
#













window.mainloop()