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
        tuple: A tuple containing the validated birthdate as a datetime object or None,
               and an error message if the date is invalid or None if the date is valid.
    """
    
    try:
        # Attempt to convert birthday string to datetime object
        valid_birthdate = datetime.datetime.strptime(birthdate_str, "%d-%m-%Y").date()

        # Check if the birthdate is in the future
        if valid_birthdate > datetime.datetime.now().date():
            return None, "Birthdate cannot be in the future."

        # Return the valid birthdate and None for the error message
        return valid_birthdate, None
    
    except ValueError:
        # Return None and the error message when format is invalid
        return None, "Invalid date format. Please use dd-mm-yyyy."