import tkinter as tk
import data_quiz

PALE_YELLOW = "#F5EFE6"
BLUE = "#BCD2E8"
GREEN = "#80ef80"

class CategoryUI:
    
    def __init__(self, start_quiz_callback):
        self.start_quiz_callback = start_quiz_callback
        self.window = tk.Tk()
        self.window.title("Millionaire Maker")
        self.window.configure(bg=PALE_YELLOW, padx=30, pady=30)
        self.window.geometry("500x650")

        self.main_label = tk.Label(self.window, text="Welcome to Millionaire Maker!", bg=PALE_YELLOW, fg=GREEN, font=("Courier New", 30, "bold"), wraplength=400)
        self.main_label.grid(row=1, column=1, columnspan=2)

        self.category_label = tk.Label(self.window, text="Which category would you like to choose?", bg=PALE_YELLOW, fg=BLUE, font=("Courier New", 28, "bold"), wraplength=400)
        self.category_label.grid(row=2, column=1, padx=20, pady=20, columnspan=2)

        self.gk_button = tk.Button(self.window, text="General Knowledge", font=("Courier New", 18), command=lambda: self.set_category(9))
        self.gk_button.grid(row=3, column=1, padx=20, pady=10)

        self.sn_button = tk.Button(self.window, text="Science & Nature", font=("Courier New", 18), command=lambda: self.set_category(17))
        self.sn_button.grid(row=4, column=1, padx=20, pady=10)

        self.comp_button = tk.Button(self.window, text="Computers", font=("Courier New", 18), command=lambda: self.set_category(18))
        self.comp_button.grid(row=5, column=1, padx=20, pady=10)

    def set_category(self, category_id):
        data_quiz.parameters["category"] = category_id
        self.window.destroy()  # Close category selection window
        self.start_quiz_callback()  # Callback to start quiz
