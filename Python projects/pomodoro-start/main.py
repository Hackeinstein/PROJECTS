from tkinter import *
import time
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer=""


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_txt.config(text="Timer")
    tick_txt.config(text="")
    global reps
    reps=0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps == 0 or reps == 1 or reps == 3 or reps == 5 or reps == 7:
        count_down(WORK_MIN * 60)
        timer_txt.config(text="WORK", fg=GREEN)
    elif reps == 2 or reps == 4 or reps == 6:
        count_down(SHORT_BREAK_MIN * 60)
        timer_txt.config(text="BREAK", fg=PINK)
    elif reps == 8:
        count_down(LONG_BREAK_MIN * 20)
        timer_txt.config(text="LONG BREAK", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps > 1 and reps % 2 > 1:
            tick_txt["text"] += "✔"


# ---------------------------- UI SETUP ------------------------------- #
# window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# canvas for tomato image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# timer text
timer_txt = Label(text="Timer", font=(FONT_NAME, "40", "bold"), fg=GREEN, bg=YELLOW)
timer_txt.grid(column=1, row=0)
# start btn
start_btn = Button(text="Start", command=start_timer)
start_btn.grid(column=0, row=2)
# tick label
tick_txt = Label(text="", fg=GREEN, bg=YELLOW)
tick_txt.grid(column=1, row=3)
# reset btn
reset_btn = Button(text="Reset", command=reset_timer)
reset_btn.grid(column=2, row=2)

window.mainloop()
