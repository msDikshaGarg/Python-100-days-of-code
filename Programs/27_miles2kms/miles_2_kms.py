import tkinter as tk

# Create a main window
root = tk.Tk()

# Title
root.title("Miles to Kilometer Converter")

# Label
label1 = tk.Label(text="Convert miles to kms!")
label1.grid(row = 1, column = 2, padx = 10, pady = 10)

# Miles Entry
miles = tk.Entry()
miles.configure(width = 5)
miles.grid(row = 2, column = 1, padx = 2, pady = 10)
miles.insert(0, 1)

# Label 
label2 = tk.Label(text="mi =")
label2.grid(row = 2, column = 2, pady = 10)

# Label 
label3 = tk.Label(text = "1.61 kms")
label3.grid(row = 2, column = 3, pady = 10)

def convert_miles():
    miles_input =  miles.get()
    kms = float(miles_input) * 1.60934
    new_val = str(round(kms, 2)) + ' kms'
    label3.config(text = new_val)

# Create a bottom
conv_btn=tk.Button(text = 'Convert', command=convert_miles)
conv_btn.grid(row = 3, column = 2, pady = 10)

# Run the main event loop
root.mainloop()