#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 19:29:40 2024

@author: brendangallagher
"""

import csv


def find_star_by_distance(target_value):
    
    """
    Finds the star in the provided CSV file that is closest to the target 
    distance in light-years.

    Args:
        target_value (float): The target distance in light-years.

    Returns:
        tuple: A tuple containing the name of the closest star (potentially 
        using either 'proper', 'gl', or 'hyg' identifiers) and the 
        constellation it belongs to, or None and None if no star data 
        is found.
    """

    # Initialise variables
    closest_star = None
    closest_distance = float('inf')
    closest_constellation = None

    try:
        with open('data/star_data.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                
                # Check if distance data is present and valid
                if 'dist_ly' in row:
                    try:
                        star_distance = float(row['dist_ly'])
                    except ValueError:
                        continue

                    # Calculate distance from target and update if closer
                    distance = abs(target_value - star_distance)
                    
                    if distance < closest_distance:
                        
                        # Prioritize using more specific star identifiers
                        if row['proper']:
                            closest_star = row['proper']
                            
                        elif row['gl']:
                            closest_star = row['gl']
                            
                        else:
                            closest_star = row['hyg']
                            
                        closest_constellation = row['constellation']
                        closest_distance = distance

    except FileNotFoundError:
        print("Star data file not found.")

    return closest_star, closest_constellation


def find_closest_values(df, target_value):
    
    """
    Finds the value in the specified DataFrame column that is closest to the 
    target value.

    Args:
        df (pandas.DataFrame): The DataFrame containing the values.
        target_value (float): The target value.

    Returns:
        float: The value in the 'dist_ly' column of the DataFrame that is 
        closest to thetarget value.
    """

    # Use optimized method to find closest value index
    closest_index = (df['dist_ly'] - target_value).abs().idxmin()
    closest_value = df['dist_ly'][closest_index]

    return closest_value


