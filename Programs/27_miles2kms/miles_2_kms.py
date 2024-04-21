import tkinter as tk

# Create a main window
root = tk.Tk()

# Title
root.title("Miles to Kms Converter")

# Label
label1 = tk.Label(text="Convert miles to kms!")
label1.grid(row = 1, column = 2, padx = 10, pady = 10)

# Miles Entry
#miles_text = tk.StringVar()
miles = tk.Entry()
#mile_1 = "1"
#miles_text.set(mile_1)
miles.configure(width = 5)
miles.grid(row = 2, column = 1, padx = 2, pady = 10)

# Label 
label2 = tk.Label(text="miles =")
label2.grid(row = 2, column = 2, pady = 10)

def convert_miles():
    miles_input =  miles.get()
    kms = miles * 1.60934
    return None

# Label 
label3 = tk.Label(text = "0 kms")
label3.grid(row = 2, column = 3, pady = 10)

# Create a bottom
conv_btn=tk.Button(root,text = 'Convert')
conv_btn.grid(row = 3, column = 2, pady = 10)

# Run the main event loop
root.mainloop()