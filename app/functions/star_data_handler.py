#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 18:44:00 2024

@author: brendangallagher
"""

import csv

def extract_star_info(star_name):
    try:
        with open('data/star_data.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if star_name in [row['proper'], row['gl'], row['hyg']]:
                    return row
    except FileNotFoundError:
        print("Star data file not found.")
    return None

def star_data_finder(closest_star):
    star_name = closest_star
    star_info = extract_star_info(star_name)
    if star_info:
        proper_name = star_info['proper']
        gaia_name = star_info['gl']
        hyg_name = star_info['hyg']
        id_name = star_info['id']
        distance_lightyears = star_info['dist_ly']
        const = star_info['constellation']
        mag = star_info['mag']
        absmag = star_info['absmag']
        spect = star_info['spect']
        ra = star_info['ra']
        dec = star_info['dec']
        
    else:
        print("Star not found in the database.")
        
    return proper_name, gaia_name, hyg_name, id_name, distance_lightyears,\
        const, mag, absmag, spect, ra, dec
