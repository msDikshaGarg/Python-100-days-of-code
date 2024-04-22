import tkinter as tk

# Color palette
LIGHT_PINK = "#FFE6E6"
PINK = "#E1AFD1"
LAVENDER = "#AD88C6"
VIOLET = "#7469B6"

# Time presets
WORK = 25
SMALL_BREAK = 5
BIG_BREAK = 20
stage = 1

# Timer function
def timer_countdown(time_val):
    global stage 
    if time_val == 0:
        stage += 1
        print(stage)
    if time_val > 0:
        print(time_val)
        window.after(10, timer_countdown, time_val - 1)

def set_timer():
    if stage <= 9:
        if stage in [1, 3, 5, 7]:
            timer_countdown(WORK)
        elif stage in [2, 4, 6, 8]:
            timer_countdown(SMALL_BREAK)
        elif stage == 9: 
            timer_countdown(BIG_BREAK)
    

# Window 
window = tk.Tk()
window.title("Pomodoro Timer")
window.configure(bg=LIGHT_PINK)
window.geometry("870x800")

set_timer()


# Heading label
heading = tk.Label(text = "Pomodoro Timer", bg=LIGHT_PINK, fg=LAVENDER, font = ("Helvetica", 50, "bold"))
heading.grid(row = 1, column = 2, padx = 10, pady = 10)

# Main image and text
canvas = tk.Canvas(window, width = 500, height = 500, highlightthickness=0)
tomato_photo = tk.PhotoImage(file = "tomato.png")
canvas.create_image(250, 250, image = tomato_photo)
canvas.create_text(250, 330, text = "00:00", fill = VIOLET, font = ("Helvetica", 35, "bold"))
canvas.grid(row = 2, column = 2)

# Step Label
step = tk.Label(text = "#1", bg=LIGHT_PINK, fg=LAVENDER, font = ("Helvetica", 35, "bold"))
step.grid(row = 3, column = 2, padx = 10, pady = 10)

# Start Button
start_button=tk.Button(text = 'Start', font = ("Helvetica", 20, "bold"), width=10, height=2, fg = LAVENDER)
start_button.grid(row = 3, column = 1, padx = 10, pady = 10)

# Reset Button
reset_button=tk.Button(text = 'Reset', font = ("Helvetica", 20, "bold"), width=10, height=2, fg = LAVENDER)
reset_button.grid(row = 3, column = 3, padx = 10, pady = 10)


window.mainloop()
