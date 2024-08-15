from tkinter import *
from math import *

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
time_left = 0  # Variable to store remaining time when stopped
is_work_session = False  # Flag to track if the current session is a work session

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps, time_left, timer, is_work_session
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    reps = 0
    time_left = 0
    is_work_session = False
    start_button.config(state=NORMAL)  # Re-enable the Start button

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps, time_left, is_work_session
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        time_left = long_break_sec
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
        is_work_session = False
    elif reps % 2 == 0:
        time_left = short_break_sec
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
        is_work_session = False
    else:
        time_left = work_sec
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
        is_work_session = True  # Mark this as a work session
    
    start_button.config(state=DISABLED)  # Disable the Start button during the session

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global time_left, timer
    time_left = count  # Update the remaining time
    
    count_min = floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}" 
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_button.config(state=NORMAL)  # Re-enable the Start button after the session ends
        start_timer()
        mark = ""
        work_sessions = floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✅"
        check_marks.config(text=mark)
            
# ---------------------------- STOP MECHANISM ------------------------------- #

def stop_time():
    global timer, time_left
    if is_work_session:  # Only allow stopping during a work session
        if timer is not None:
            window.after_cancel(timer)  # Stop the countdown
            title_label.config(text="Stopped")
            start_button.config(state=NORMAL)  # Re-enable the Start button when stopped

# ---------------------------- RESUME TIME MECHANISM ------------------------------- #

def resume_timer():
    global time_left
    if time_left > 0:
        count_down(time_left)
        title_label.config(text="Resumed")
        start_button.config(state=DISABLED)  # Disable the Start button when resuming

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./DAY_28/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

stop_button = Button(text="Stop", highlightthickness=0, command=stop_time)
stop_button.grid(column=0, row=4)

resume_button = Button(text="Resume", highlightthickness=0, command=resume_timer)
resume_button.grid(column=2, row=4)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
