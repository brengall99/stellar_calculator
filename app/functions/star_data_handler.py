#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 18:44:00 2024

@author: brendangallagher
"""

import csv


def extract_star_info(star_name):
    
    """
    Extracts star information from the CSV file.

    Args:
        star_name (str): The name of the star to find (either 'proper', 
        'gl', or 'hyg' identifier).

    Returns:
        dict: A dictionary containing all available star information if found, 
        or None if not found.
    """

    try:
        with open('data/star_data.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                # Check if any of the star identifiers match the input name
                if star_name in [row['proper'], row['gl'], row['hyg']]:
                    
                    return row  # Return the entire row dictionary if found
                
    except FileNotFoundError:
        print("Star data file not found.")

    return None  # Return None if the star information is not found


def star_data_finder(closest_star):
    
    """
    Fetches detailed information about the given star name.

    Args:
        closest_star (str): The name of the star (potentially using 'proper', 
        'gl', or 'hyg' identifier).

    Returns:
        tuple: A tuple containing various star information (proper name, 
        Gaia name, etc.) if found, or 11 None values if not found.
    """

    star_name = closest_star  # Assign variable for clarity
    star_info = extract_star_info(star_name)  # Get star info

    if star_info:
        # Extract detailed information from the returned dictionary
        proper_name = star_info['proper']
        gaia_name = star_info['gl']
        hyg_name = star_info['hyg']
        id_name = star_info['id']
        distance_lightyears = star_info['dist_ly']
        constellation = star_info['constellation']
        mag = star_info['mag']
        absmag = star_info['absmag']
        spect = star_info['spect']
        ra = star_info['ra']
        dec = star_info['dec']

        return proper_name, gaia_name, hyg_name, id_name, \
            distance_lightyears, constellation, mag, absmag, spect, ra, dec
            
    else:
        print("Star not found in the database.")
        # Return None values if the star information is not found
        return None, None, None, None, None, None, None, None, None, None, None
