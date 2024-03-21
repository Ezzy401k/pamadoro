from tkinter import *

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
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer1, text="00:00")
    label.config(text="Timer")
    check.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    reps += 1
    if reps % 2 == 1:
        label.config(text="Work", foreground=GREEN)
        counter(work_sec)

    elif reps % 8 == 0:
        label.config(text="Break", foreground=RED)
        counter(long_break)

    elif reps % 2 == 0:
        label.config(text="Break", foreground=PINK)
        counter(short_break)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def counter(count):
    global timer
    count_min = count // 60
    count_sec = count % 60

    if count_sec in range(0, 10):
        count_sec = f"0{count_sec}"

    if count_min in range(0, 10):
        count_min = f"0{count_min}"

    canvas.itemconfig(timer1, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, counter, count - 1)
    else:
        start_timer()
        mark = ""
        for i in range(reps // 2):
            mark += "✔"
        check.config(text=mark)


# ------------ ---------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.minsize(350, 400)
window.maxsize(350, 400)
window.config(padx=50, pady=30, bg=YELLOW)

canvas = Canvas(width=200, height=226, bg=YELLOW, highlightthickness=0)
picture = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=picture)
timer1 = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

label = Label(text="Timer", bg=YELLOW, foreground=GREEN, font=(FONT_NAME, 35, "bold"))
label.grid(column=1, row=0)

start = Button(text="Start", command=start_timer)
start.grid(column=0, row=2)

restart = Button(text="Reset", command=reset_timer)
restart.grid(column=2, row=2)

check = Label(bg=YELLOW, foreground=GREEN, font=(FONT_NAME, 15, "bold"))
check.grid(column=1, row=3)

window.mainloop()
