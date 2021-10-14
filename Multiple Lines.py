import tkinter as tk
from tkinter import ttk

# Create the application window
window = tk.Tk()

# Create the user interface
my_label = ttk.Label(window, text="This is a line of text")
my_label.grid(row=1, column=1)
my_label2 = ttk.Label(window, text="Here's another line.")
my_label2.grid(row=2, column=1)

# Start the GUI event loop
window.mainloop()

