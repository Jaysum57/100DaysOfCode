from tkinter import *
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
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_clicked():
    global reps
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_clicked():
    global reps
    reps +=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    #If it's the 1st/3rd/7th rep:
    if reps in [1,3,7]: #green
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)

    #If it's the 8th rep:
    elif reps == 8: #pink
        timer_label.config(text="Short Break", fg=PINK)
        count_down(long_break_sec)

    #If it's the 2nd/4th/rep:
    elif reps in [2,4]: #red
        timer_label.config(text="Break",fg=RED)
        count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count > 0:
        global timer
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}" )
        timer = window.after(1000, count_down, count -1)
    
    else:
        start_clicked()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✓"
            check_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

##Timer label
timer_label = Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

 
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Buttons

#Start button

start_button = Button(text="Start", command=start_clicked)
start_button.grid(column=0, row=2)

#Reset button

button = Button(text="Reset", command=reset_clicked)
button.grid(column=2, row=2)

# Checks Label
check_label = Label(text="", font=(FONT_NAME, 24, "bold"), fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)



window.mainloop()