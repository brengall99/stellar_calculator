#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 19:34:59 2024

@author: brendangallagher
"""

import datetime

def validate_birthdate(birthdate_str):
    
    """
    Validates a birthdate string in the format dd-mm-yyyy.

    Args:
        birthdate_str (str): The birthdate string to validate.

    Returns:
        datetime.date: The validated birthdate as a datetime object, 
        or None if invalid.
    """
    
    try:
        # Attempt to convert birthday string to datetime object
        birthdate = datetime.datetime.strptime(birthdate_str, "%d-%m-%Y")
        
        # Check if the birthdate is in the future and raise error
        if birthdate > datetime.datetime.now():
            print("Birthdate cannot be in the future.")
            return None
        
        # Return the valid birthdate
        return birthdate
    
    except ValueError:
        #  Handle errors when format is invalid
        print("Invalid date format. Please use dd-mm-yyyy.")
        return None