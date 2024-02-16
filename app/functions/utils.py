#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 19:34:59 2024

@author: brendangallagher
"""

import datetime

def validate_birthdate(birthdate_str):
    try:
        birthdate = datetime.strptime(birthdate_str, "%d-%m-%Y")
        if birthdate > datetime.now():
            print("Birthdate cannot be in the future.")
            return None
        return birthdate
    except ValueError:
        print("Invalid date format. Please use dd-mm-yyyy.")
        return None