#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 19:42:05 2024

@author: brendangallagher
"""

#-----------------------------------------------------------------------------/
import pandas as pd
from functions.age_calculator import AgeCalculator
from functions.star_data_handler import star_data_finder
from functions.distance_utils import find_star_by_distance, find_closest_values 
from functions.constellation_loader import load_constellation_data
from functions.utils import validate_birthdate
#-----------------------------------------------------------------------------/
        
def main():
    while True:
        birthdate_str = \
            input("\nEnter your birthdate in dd-mm-yyyy format: ")
        birthdate = validate_birthdate(birthdate_str)
        if birthdate:
            break
    
    age_years, age_days, age_hours, age_minutes\
        = AgeCalculator.calculate_age(birthdate)
    
    time_life = age_years + (age_days/365.25) + (age_hours/(365.25*24))\
        + (age_minutes/(365.25*24*60))
    
    # Use find_closest_values function to find the target value
    df = pd.read_csv('data/star_data.csv')
    target_value = find_closest_values(df, time_life)
    
    # Find information about the closest star
    closest_star, closest_constellation\
        = find_star_by_distance(target_value)
    
    # Load constellation data
    constellation_data = load_constellation_data()
    
    # Get the name of the closest constellation
    closest_constellation_name = \
        constellation_data.get(closest_constellation, closest_constellation)
    
    # Calculate the light age of the target value
    light_age_years, light_age_days, light_age_hours, light_age_minutes\
        = AgeCalculator.calculate_light_age(target_value)
    
    # Print information
    print(f"\nYour current age is {age_years} years, {age_days} days, "
          f"{age_hours} hours, and {age_minutes} minutes old.")
    print(f"\nThe light from the star '{closest_star}', in the constellation "
          f"{closest_constellation_name}, is the star that emitted light"
          " closest to your birth")
    print(f"\nLight from '{closest_star}' was emitted approximately "
          f"{light_age_years} years, {light_age_days} days, {light_age_hours} "
          f"hours, and {light_age_minutes} minutes ago.")
    
    proper_name, gaia_name, hyg_name, id_name, distance_lightyears,\
        const, mag, absmag, spect, ra, dec = star_data_finder(closest_star)

if __name__ == "__main__":
    main()
    
    
#-----------------------------------------------------------------------------/




    
    
    
    
    