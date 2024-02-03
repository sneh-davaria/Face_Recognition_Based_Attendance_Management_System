import tkinter as tk
import sys
import os
from tkinter import *

# Create the main window
root = tk.Tk()
root.title("Attendance Managment")
root.geometry("720x480")

# Create a frame to hold the buttons
button_frame = tk.Frame(root)
button_frame.pack()


def run():
    os.system('main.py')


# Create the "Attendance Report" button
attendance_button = tk.Button(
    button_frame, text="Attendance Report", height=20, width=30)
attendance_button.pack(side=tk.LEFT, padx=10, pady=10,)

# Create the "Admin" button
admin_button = tk.Button(button_frame, text="Admin",
                         height=20, width=30, command=run)
admin_button.pack(side=tk.LEFT, padx=10, pady=10)


# Start the main event loop
root.mainloop()
