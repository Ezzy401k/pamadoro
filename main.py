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

# Function to reset the timer
def reset_timer():
    window.after_cancel(timer)  # Cancel the timer
    canvas.itemconfig(timer1, text="00:00")  # Reset the timer display on the canvas
    label.config(text="Timer")  # Reset the label text
    check.config(text="")  # Reset the checkmark display
    global reps
    reps = 0  # Reset the number of repetitions


# ---------------------------- TIMER MECHANISM ------------------------------- #
# Function to start the timer
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    reps += 1  # Increment the number of repetitions
    if reps % 2 == 1:
        label.config(text="Work", foreground=GREEN)  # Change label text to "Work" with green color
        counter(work_sec)  # Start the work timer

    elif reps % 8 == 0:
        label.config(text="Break", foreground=RED)  # Change label text to "Break" with red color
        counter(long_break)  # Start the long break timer

    elif reps % 2 == 0:
        label.config(text="Break", foreground=PINK)  # Change label text to "Break" with pink color
        counter(short_break)  # Start the short break timer


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# Function to handle the countdown
def counter(count):
    global timer
    count_min = count // 60
    count_sec = count % 60

    if count_sec in range(0, 10):
        count_sec = f"0{count_sec}"

    if count_min in range(0, 10):
        count_min = f"0{count_min}"

    canvas.itemconfig(timer1, text=f"{count_min}:{count_sec}")  # Update the timer display on the canvas
    if count > 0:
        timer = window.after(1000, counter, count - 1)  # Call the counter function after 1 second
    else:
        start_timer()  # Start the timer again when the countdown reaches 0
        mark = ""
        for i in range(reps // 2):
            mark += "✔"  # Add checkmarks for completed work cycles
        check.config(text=mark)  # Update the checkmark display


# ------------ ---------------- UI SETUP ------------------------------- #
window = Tk()  # Create the main tkinter window
window.title("Pomodoro")  # Set the title of the window
window.minsize(350, 400)  # Set the minimum size of the window
window.maxsize(350, 400)  # Set the maximum size of the window
window.config(padx=50, pady=30, bg=YELLOW)  # Set padding and background color

canvas = Canvas(width=200, height=226, bg=YELLOW, highlightthickness=0)  # Create a canvas for the tomato image
picture = PhotoImage(file="tomato.png")  # Load the tomato image
canvas.create_image(100, 110, image=picture)  # Add the tomato image to the canvas
timer1 = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))  # Timer display
canvas.grid(column=1, row=1)  # Grid layout for canvas

label = Label(text="Timer", bg=YELLOW, foreground=GREEN, font=(FONT_NAME, 35, "bold"))  # Timer label
label.grid(column=1, row=0)  # Grid layout for label

start = Button(text="Start", command=start_timer)  # Start button
start.grid(column=0, row=2)  # Grid layout for start button

restart = Button(text="Reset", command=reset_timer)  # Reset button
restart.grid(column=2, row=2)  # Grid layout for reset button

check = Label(bg=YELLOW, foreground=GREEN, font=(FONT_NAME, 15, "bold"))  # Checkmark label
check.grid(column=1, row=3)  # Grid layout for checkmark label

window.mainloop()  # Run the tkinter event loop
