#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 19:33:06 2024

@author: brendangallagher
"""

import csv

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