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


def create_results():
    # Function to create the result widgets, initially without packing them into the GUI
    global output_text, star_info_text, output_frame, star_info_frame, plot_frame

    # Create a frame to display the output text
    output_frame = tk.Frame(root)

    output_text = tk.Text(output_frame, height=10, width=80)
    output_text.pack()

    # Create a frame to display the additional star information
    star_info_frame = tk.Frame(root)

    star_info_text = tk.Text(star_info_frame, height=14, width=80)
    star_info_text.pack()

    # Create a frame to hold the plot
    plot_frame = tk.Frame(root)

def show_results():
    # Function to pack the result widgets into the GUI when 'Run Program' is clicked
    output_frame.pack(pady=10, fill=tk.BOTH, expand=True)
    star_info_frame.pack(pady=10, fill=tk.BOTH, expand=True)
    plot_frame.pack(fill=tk.BOTH, expand=True)


def run_program(birthdate_str):
    global output_text, star_info_text, plot_frame
    
    birthdate, error_message = validate_birthdate(birthdate_str)
    if birthdate:
        
        #output_text.delete(1.0, tk.END)
        
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
        
        create_results()
        show_results()

        # Clear the previous plot in the plot_frame
        for widget in plot_frame.winfo_children():
            widget.destroy()

        # Create a canvas and add the plot to the Tkinter window inside the frame
        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas.draw()
        
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Fetch the star information to display
        proper_name, gaia_name, hyg_name, id_name, distance_lightyears, \
        const, mag, absmag, spect, ra, dec = star_data_finder(closest_star)
        
        ra = float(ra)*24
        ra_formatted = "{:.2f}".format(ra) if isinstance(ra, float) else "N/A"
    
        # Display the additional star information in the GUI
        if proper_name or gaia_name or id_name:
            star_info = f"\nStar Information:\n"
            star_info += f"Proper Name: {proper_name}\n" if proper_name else ""
            star_info += f"Gaia Name: {gaia_name}\n" if gaia_name else ""
            star_info += f"HYG Name: {hyg_name}\n" if hyg_name else ""
            star_info += f"ID: {id_name}\n" if id_name else ""
            star_info += f"Distance (light-years): {distance_lightyears}\n" if distance_lightyears else ""
            star_info += f"Constellation: {const}\n" if const else ""
            star_info += f"Magnitude: {mag}\n" if mag else ""
            star_info += f"Absolute Magnitude: {absmag}\n" if absmag else ""
            star_info += f"Spectral Type: {spect}\n" if spect else ""
            star_info += f"Right Ascension: {ra_formatted}\n" if ra_formatted else ""
            star_info += f"Declination: {dec}\n" if dec else ""
    
            star_info_text.delete(1.0, tk.END)
            star_info_text.insert(tk.END, star_info)
        else:
            star_info_text.delete(1.0, tk.END)
            star_info_text.insert(tk.END, "No additional information available for this star.")

        # Display the information in the GUI
        info_text = f"\nYour current age is {age_years} years, {age_days} days, {age_hours} hours, and {age_minutes} minutes old.\n"
        info_text += f"\nThe light from the star '{closest_star}', in the constellation {closest_constellation_name}, is the \n"
        info_text += "star that emitted light closest to your birth.\n"
        info_text += f"\nLight from '{closest_star}' was emitted approximately {light_age_years} years, {light_age_days} days, {light_age_hours} hours,\n"
        info_text += f"and {light_age_minutes} minutes ago."

        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, info_text)
        
    else:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, error_message)
        
def reset_program():
    global output_text, star_info_text, plot_frame
    # Clear the existing data in text widgets and plot frame
    output_text.delete(1.0, tk.END)
    star_info_text.delete(1.0, tk.END)
    
    # Clear the plot frame
    for widget in plot_frame.winfo_children():
        widget.destroy()

    # Optionally, reset the birthdate entry field
    birthdate_entry.delete(0, tk.END)

# Create the main application window
root = tk.Tk()
create_results()
root.title("Star Plotting Program")

def get_birthdate(event=None):  # Allow for the event parameter, which is passed by the bind method
    birthdate_str = birthdate_entry.get()
    run_program(birthdate_str)

# GUI setup including input for the birthdate
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

birthdate_label = tk.Label(input_frame, text="Enter your birthdate (dd-mm-yyyy):")
birthdate_label.pack(side=tk.LEFT)

birthdate_entry = tk.Entry(input_frame)
birthdate_entry.pack(side=tk.LEFT)
birthdate_entry.bind("<Return>", get_birthdate)  # Bind the Enter key to get_birthdate function

run_button = tk.Button(input_frame, text="Run Program", command=get_birthdate)
run_button.pack(side=tk.LEFT)

# Function to close the GUI
def close_gui():
    root.destroy()
    
button_frame = tk.Frame(root)
button_frame.pack(pady=10)
    
# Create a button to reset the program
reset_button = tk.Button(button_frame, text="Reset Program", command=reset_program)
reset_button.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)

# Create a button to close the GUI
exit_button = tk.Button(button_frame, text="Exit Program", command=close_gui)
exit_button.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)

root.mainloop()