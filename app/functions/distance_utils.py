#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 19:29:40 2024

@author: brendangallagher
"""

import csv

def find_star_by_distance(target_value):
    closest_star = None
    closest_distance = float('inf')
    closest_constellation = None

    try:
        with open('data/star_data.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if 'dist_ly' in row:
                    try:
                        star_distance = float(row['dist_ly'])
                    except ValueError:
                        continue  
                    distance = abs(target_value - star_distance)
                    if distance < closest_distance:
                        if row['proper']:  # Use 'proper' if available
                            closest_star = row['proper']
                        elif row['gl']:  # Use 'gl' if 'proper' empty
                            closest_star = row['gl']
                        elif row['hyg']:  # Use 'hyg' if 'proper' & 'gl' empty
                            closest_star = row['hyg']
                        closest_constellation = row['constellation']
                        closest_distance = distance

    except FileNotFoundError:
        print("Star data file not found.")

    return closest_star, closest_constellation

def find_closest_values(df, target_value):
    # Find index of closest value to the target value
    closest_index = (df['dist_ly'] - target_value).abs().idxmin()
    closest_value = df['dist_ly'][closest_index]
    return closest_value