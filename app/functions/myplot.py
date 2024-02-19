#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 08:50:33 2024

@author: brendangallagher
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from astropy.coordinates import SkyCoord
import astropy.units as u
from matplotlib.figure import Figure

def load_and_prepare_data(file_path):
    # Load the CSV data
    star_data = pd.read_csv(file_path)
    # Convert Right Ascension from hours to degrees
    star_data['ra_degrees'] = star_data['ra'] * 15
    # Convert RA and Dec to radians, adjusting for the Aitoff projection
    star_data['ra_rad'] = np.radians(star_data['ra_degrees'] - 180)
    star_data['dec_rad'] = np.radians(star_data['dec'])
    return star_data

def get_star_label(row):
    # Determine the label for the star based on available data
    if pd.notnull(row['proper']) and row['proper'] != '':
        return row['proper']
    elif pd.notnull(row['gl']) and row['gl'] != '':
        return row['gl']
    else:
        return f"ID: {row['id']}"

def plot_milky_way(ax):
    # Function to plot the Milky Way plane
    galactic_longitudes = np.linspace(0, 360, num=500)
    ra_points = []
    dec_points = []

    for l in galactic_longitudes:
        # Convert each galactic coordinate to equatorial coordinates
        galactic_coord = SkyCoord(l=l * u.degree, b=0 * u.degree, \
                                  frame='galactic')
        equatorial_coord = galactic_coord.icrs
        ra_points.append(equatorial_coord.ra.degree)
        dec_points.append(equatorial_coord.dec.degree)

    # Convert RA and Dec points to radians and adjust for the Aitoff projection
    ra_rad = np.radians(np.array(ra_points) - 180)
    dec_rad = np.radians(np.array(dec_points))

    # Plot the Milky Way plane
    ax.plot(ra_rad, dec_rad, color='lightgreen', linestyle='-', \
            linewidth=1, alpha=0.7, label='Milky Way Plane')
    return ax

def plot_stars(star_data, highlight_identifier=None, dpi=100):
    # Create a Figure object
    fig = Figure(figsize=(10, 5), dpi=dpi)
    ax = fig.add_subplot(111, projection="aitoff")
    ax.set_title("Stars on Aitoff Projection")
    
    # Normalize the magnitude to a scale suitable for marker size
    max_marker_size = 10
    min_marker_size = 1
    # Invert the magnitude since a lower magnitude number means a brighter star
    star_data['mag_scaled'] = star_data['mag'] - star_data['mag'].min()
    star_data['mag_scaled'] = (1 - (star_data['mag_scaled'] / star_data['mag_scaled'].max())) * (max_marker_size - min_marker_size) + min_marker_size
    
    # Plot all stars without labels as they won't be individually identified in the legend
    ax.scatter(star_data['ra_rad'], star_data['dec_rad'], s=star_data['mag_scaled'], alpha=0.5, color='blue')
    
    # Plot the Milky Way plane and celestial equator with labels for the legend
    ax = plot_milky_way(ax)
    ra_celestial_equator = np.linspace(-180, 180, 500)
    dec_celestial_equator = np.zeros_like(ra_celestial_equator)
    ra_celestial_equator_rad = np.radians(ra_celestial_equator)
    dec_celestial_equator_rad = np.radians(dec_celestial_equator)
    ax.plot(ra_celestial_equator_rad, dec_celestial_equator_rad, color='green', lw=1, label='Celestial Equator')
    
    # Ensure gridlines are displayed
    ax.grid(True, which='both', axis='both', color='gray', linestyle='--', linewidth=0.5)
    
    # Highlight Polaris with a label if present
    polaris = star_data[star_data['hip'] == 11767]
    if not polaris.empty:
        ax.scatter(polaris['ra_rad'], polaris['dec_rad'], s=50, color='green', label='Polaris')
    
    if highlight_identifier is not None:
        # Determine whether the identifier is likely an ID or a name
        try:
            # Attempt to convert to an integer; if this works, it's an ID
            highlight_id = int(highlight_identifier)
            highlight_star = star_data[star_data['id'] == highlight_id]
        except ValueError:
            # If conversion fails, it's not a numeric ID; treat as a name
            highlight_star = star_data[(star_data['proper'] == highlight_identifier) | (star_data['gl'] == highlight_identifier)]
        
        if not highlight_star.empty:
            ax.scatter(highlight_star['ra_rad'], highlight_star['dec_rad'], s=50, color='red', label=f"Highlighted: {highlight_identifier}")
        else:
            print(f"No star found with identifier: {highlight_identifier}")

    # Your existing code to finalize the plot...
    ax.legend(loc='upper right')
    return fig

if __name__ == "__main__":
    file_path = 'data/star_data.csv'  # Update this path to your CSV file
    highlight_identifier = '11767'  # Adjust as needed for testing
    star_data = load_and_prepare_data(file_path)
    plot_stars(star_data, highlight_identifier=highlight_identifier, dpi=100)