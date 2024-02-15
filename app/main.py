#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 19:42:05 2024

@author: brendangallagher
"""


import csv
import pandas as pd
from datetime import datetime
from calculators.find_closest_star import find_closest_values
from calculators.age_calculator import AgeCalculator

def load_constellation_data():
    constellation_data = {}
    try:
        with open('data/constellation_data.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                constellation_data[row['IAU code']] = row['Latin name']
    except FileNotFoundError:
        print("Constellation data file not found.")
    return constellation_data

def find_closest_star(age_years):
    
    closest_star = None
    closest_distance = float('inf')
    next_closest_star = None
    next_closest_distance = float('inf')
    closest_constellation = None
    proper_distance_ly = 0.0

    try:
        with open('data/star_data.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if 'dist_ly' in row:
                    try:
                        star_distance = float(row['dist_ly'])
                    except ValueError:
                        continue  
                    distance = abs(age_years - star_distance)
                    if distance < closest_distance:
                        next_closest_star = closest_star
                        next_closest_distance = closest_distance
                        closest_star = row['proper'] if row['proper'] else row['gl']
                        closest_constellation = row['constellation']
                        closest_distance = distance
                        proper_distance_ly = star_distance  

                    elif distance < next_closest_distance:
                        next_closest_star = row['proper'] if row['proper'] else row['gl']
                        next_closest_distance = distance

    except FileNotFoundError:
        print("Star data file not found.")

    return closest_star, closest_distance, closest_constellation, proper_distance_ly, next_closest_star, next_closest_distance

def main():
    birthdate_str = input(print("Birthdate: "))
    try:
        birthdate = datetime.strptime(birthdate_str, "%d-%m-%Y")
    except ValueError:
        print("Invalid date format. Please use dd-mm-yyyy.")
        return
    
    age_years, age_days, age_hours, age_minutes = AgeCalculator.calculate_age(birthdate)
    
    closest_star, closest_distance, closest_constellation_iau, proper_distance_ly, next_closest_star, next_closest_distance = find_closest_star(age_years)
    
    constellation_data = load_constellation_data()
    
    closest_constellation = constellation_data.get(closest_constellation_iau, closest_constellation_iau)
    
    # Create a DataFrame from star_data.csv
    df = pd.read_csv('data/star_data.csv')
    # Use find_closest_values function to find the target value
    target_value = find_closest_values(df, proper_distance_ly)
    
    light_age_years, light_age_days, light_age_hours, light_age_minutes = AgeCalculator.calculate_light_age(target_value)
    
    print(target_value)
    
    print(f"\nYou are {age_years} years, {age_days} days, {age_hours} hours, and {age_minutes} minutes old.")
    if closest_star:
        print(f"The light from the closest star '{closest_star}' in the constellation {closest_constellation},")
        print(f"emitted approximately {light_age_years} years, {light_age_days} days, {light_age_hours} hours,")
        print(f"and {light_age_minutes} minutes ago.")
    else:
        print("No star data found.")
    
    if next_closest_star:
        print(f"The light from the next closest star '{next_closest_star}' at a distance of {next_closest_distance} ly.")
    else:
        print("No next closest star found.")

if __name__ == "__main__":
    main()


    
    
    
    
    