import tkinter as tk

window= tk.Tk()
window.title("Miles to Km Converter")
window.config(padx = 20, pady = 20)

# is equal to
equal_label = tk.Label(text="is equal to")
equal_label.grid(column=0,row=1)

# Entry
input = tk.Entry(width=10)
input.grid(column=1,row=0)

# miles
miles_label = tk.Label(text = "Miles")
miles_label.grid(row=0,column=2)

# converted label
converted_label = tk.Label(text = "0")
converted_label.grid(row = 1, column = 1)

# km label
miles_label = tk.Label(text = "Km")
miles_label.grid(row=1,column=3)


#calculate function
def convert_to_km():
    print("Convert process")
    miles = float(input.get())
    km = (miles * 1.609344).__round__(2)
    print(type(f"{km}"))
    converted_label.config(text=f"{km}")


# calculate button
calculate_btn = tk.Button(text = "Calculate",command=convert_to_km)
calculate_btn.grid(row = 2, column = 1)






window.mainloop()