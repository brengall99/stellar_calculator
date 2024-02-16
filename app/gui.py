# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 14:21:24 2024

@author: BrendanGallagherTheH
"""

import tkinter as tk
import subprocess

def run_program(birthdate_str):
    try:
        result = subprocess.check_output(['python', 'main.py', birthdate_str], stderr=subprocess.STDOUT)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, result.decode())
    except subprocess.CalledProcessError as e:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"Error: Failed to run the program. Details: {e.output.decode()}")

def get_birthdate():
    birthdate_str = birthdate_entry.get()
    run_program(birthdate_str)

# Create the main application window
root = tk.Tk()
root.title("Program Runner")

# Create an entry for the user to input their birthdate
birthdate_label = tk.Label(root, text="Enter your birthdate (dd-mm-yyyy):")
birthdate_label.pack()

birthdate_entry = tk.Entry(root)
birthdate_entry.pack()

# Create a button to run the program
run_button = tk.Button(root, text="Run Program", command=get_birthdate)
run_button.pack()

# Create a text widget to display the output
output_text = tk.Text(root, height=10, width=50)
output_text.pack()

# Start the Tkinter event loop
root.mainloop()