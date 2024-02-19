# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 14:21:24 2024

@author: BrendanGallagherTheH
"""

import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from functions.myplot import load_and_prepare_data, plot_stars
from functions.age_calculator import AgeCalculator
from functions.star_data_handler import star_data_finder
from functions.distance_utils import find_star_by_distance, find_closest_values
from functions.constellation_loader import load_constellation_data
from functions.utils import validate_birthdate
import pandas as pd
# from functions.imports import *

def run_program(birthdate_str):
    birthdate = validate_birthdate(birthdate_str)
    if birthdate:
        age_years, age_days, age_hours, age_minutes = AgeCalculator.calculate_age(birthdate)
        time_life = age_years + (age_days / 365.25) + (age_hours / (365.25 * 24)) + (age_minutes / (365.25 * 24 * 60))

        df = pd.read_csv('data/star_data.csv')
        target_value = find_closest_values(df, time_life)
        closest_star, closest_constellation = find_star_by_distance(target_value)
        constellation_data = load_constellation_data()
        closest_constellation_name = constellation_data.get(closest_constellation, closest_constellation)

        light_age_years, light_age_days, light_age_hours, light_age_minutes = AgeCalculator.calculate_light_age(target_value)

        proper_name, gaia_name, hyg_name, id_name, distance_lightyears, const, mag, absmag, spect, ra, dec = star_data_finder(closest_star)
        
        highlight_identifier = proper_name if proper_name else (gaia_name if gaia_name else str(id_name))
        
        # Load the star data and plot with the highlight
        star_data = load_and_prepare_data('data/star_data.csv')
        fig = plot_stars(star_data, highlight_identifier=highlight_identifier, dpi=100)

        # Clear the previous plot in the plot_frame
        for widget in plot_frame.winfo_children():
            widget.destroy()

        # Create a canvas and add the plot to the Tkinter window inside the frame
        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        

        # Display the information in the GUI
        info_text = f"\nYour current age is {age_years} years, {age_days} days, {age_hours} hours, and {age_minutes} minutes old.\n"
        info_text += f"The light from the star '{closest_star}', in the constellation {closest_constellation_name}, is the star that emitted light closest to your birth.\n"
        info_text += f"Light from '{closest_star}' was emitted approximately {light_age_years} years, {light_age_days} days, {light_age_hours} hours, and {light_age_minutes} minutes ago."

        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, info_text)
    else:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Invalid birthdate input. Please use 'dd-mm-yyyy' format.")


def get_birthdate():
    birthdate_str = birthdate_entry.get()
    run_program(birthdate_str)

# Create the main application window
root = tk.Tk()
root.title("Star Plotting Program")

# GUI setup including input for the birthdate
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

birthdate_label = tk.Label(input_frame, text="Enter your birthdate (dd-mm-yyyy):")
birthdate_label.pack(side=tk.LEFT)

birthdate_entry = tk.Entry(input_frame)
birthdate_entry.pack(side=tk.LEFT)

run_button = tk.Button(input_frame, text="Run Program", command=get_birthdate)
run_button.pack(side=tk.LEFT)

# Function to close the GUI
def close_gui():
    root.destroy()

# Create a button to close the GUI
exit_button = tk.Button(root, text="Exit Program", command=close_gui)
exit_button.pack(pady=10)  # Adjust padding as needed

# Create a frame to display the output text
output_frame = tk.Frame(root)
output_frame.pack(pady=10, fill=tk.BOTH, expand=True)

output_text = tk.Text(output_frame, height=10, width=50)  # Define output_text here
output_text.pack()

# Create a frame to hold the plot
plot_frame = tk.Frame(root)
plot_frame.pack(fill=tk.BOTH, expand=True)

root.mainloop()