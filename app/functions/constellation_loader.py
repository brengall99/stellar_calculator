#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 19:33:06 2024

@author: brendangallagher
"""

import csv

def load_constellation_data():
    
    """
    Loads constellation data from a CSV file into a dictionary.

    Returns:
        dict: A dictionary mapping IAU codes to Latin constellation names.
    """

    constellation_data = {}  # Initialize dictionary

    try:
        with open('data/constellation_data.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)  # Create a CSV reader object

            for row in reader:
                # Extract IAU code and Latin name from each row
                iau_code = row['IAU code']
                latin_name = row['Latin name']

                # Add the IAU code and Latin name pair to the dictionary
                constellation_data[iau_code] = latin_name

    except FileNotFoundError:
        print("Constellation data file not found.")

    return constellation_data  # Return the populated dictionary