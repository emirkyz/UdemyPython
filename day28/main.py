import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50,bg = YELLOW)

tomoto_img = tk.PhotoImage(file="tomato.png")

canvas = tk.Canvas(width=200, height=224,bg=YELLOW,highlightthickness=0)
canvas.create_image(100, 112, image=tomoto_img)
canvas.pack()

canvas.create_text(100,130,text = "00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.create_text()
window.mainloop()