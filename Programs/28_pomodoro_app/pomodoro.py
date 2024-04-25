import tkinter as tk

# Color palette
LIGHT_PINK = "#FFE6E6"
PINK = "#E1AFD1"
LAVENDER = "#AD88C6"
VIOLET = "#7469B6"

# Time presets
WORK = 1500
SMALL_BREAK = 300
BIG_BREAK = 1200
stage = 0
timer = None

# Setting timer 
def set_timer():
    global stage 
    stage += 1
    step.config(text = f"#{stage}")
    if stage < 9:
        if stage in [1, 3, 5, 7]:
            timer_countdown(WORK)
            heading.config(text = "Work")
        elif stage in [2, 4, 6]:
            timer_countdown(SMALL_BREAK)
            heading.config(text = "Break")
        elif stage == 8: 
            timer_countdown(BIG_BREAK)
            heading.config(text = "Break")

# Timer functionality
def timer_countdown(time_val):
    time_mins = time_val // 60
    time_secs = time_val % 60

    if time_secs < 10:
        time_secs = f"0{time_secs}"

    canvas.itemconfig(timer_text, text = f"{time_mins}:{time_secs}")
    global timer
    if time_val > 0:
        timer = window.after(1000, timer_countdown, time_val - 1)
    else: 
        set_timer()

# Reset timer 
def reset_timer():
    global stage 
    stage = 0
    window.after_cancel(timer)
    heading.config(text = "Pomodoro Timer")
    step.config(text = "#1")
    canvas.itemconfig(timer_text, text = "00:00")

    
# Window mainloop
window = tk.Tk()
window.title("Pomodoro Timer")
window.configure(bg=LIGHT_PINK)
window.geometry("870x800")

# Heading label
heading = tk.Label(text = "Pomodoro Timer", bg=LIGHT_PINK, fg=LAVENDER, font = ("Helvetica", 50, "bold"))
heading.grid(row = 1, column = 2, padx = 10, pady = 10)

# Main image and text
canvas = tk.Canvas(window, width = 500, height = 500, highlightthickness=0)
tomato_photo = tk.PhotoImage(file = "tomato.png")
canvas.create_image(250, 250, image = tomato_photo)
timer_text = canvas.create_text(250, 330, text = "00:00", fill = VIOLET, font = ("Helvetica", 35, "bold"))
canvas.grid(row = 2, column = 2)

# Step Label
step = tk.Label(text = "#1", bg=LIGHT_PINK, fg=LAVENDER, font = ("Helvetica", 35, "bold"))
step.grid(row = 3, column = 2, padx = 10, pady = 10)

# Start Button
start_button=tk.Button(text = 'Start', font = ("Helvetica", 20, "bold"), width=10, height=2, fg = LAVENDER, command = set_timer)
start_button.grid(row = 3, column = 1, padx = 10, pady = 10)

# Reset Button
reset_button=tk.Button(text = 'Reset', font = ("Helvetica", 20, "bold"), width=10, height=2, fg = LAVENDER, command = reset_timer)
reset_button.grid(row = 3, column = 3, padx = 10, pady = 10)

window.mainloop()
