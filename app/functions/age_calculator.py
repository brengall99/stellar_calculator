#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 18:17:00 2024

@author: brendangallagher
"""

from datetime import datetime

class AgeCalculator:
    
    """
    Calculates age based on either a birthdate or star distance in light-years.

    Attributes:
        None
    """

    @staticmethod
    def calculate_age(birthdate):
        
        """
        Calculates age in years, days, hours, and minutes from a birthdate.

        Args:
            birthdate (datetime.date): The birthdate of the person.

        Returns:
            tuple: A tuple containing (years, days, hours, minutes).
        """

        today = datetime.now().date()
        # Calculate difference between today and birthdate
        age_delta = today - birthdate  

        years = age_delta.days // 365  # Number of whole years 
        days = age_delta.days % 365  # Remaining days

        hours, remainder = divmod(age_delta.seconds, 3600)  # Find ours
        minutes, _ = divmod(remainder, 60)  # Find minutes

        return years, days, hours, minutes

    @staticmethod
    def calculate_light_age(star_distance_ly):
        
        """
        Calculates "light age" in years, days, hours, and minutes 
        of a star based on its distance in light-years.

        Args:
            star_distance_ly (float): The distance of the star in light-years.

        Returns:
            tuple: A tuple containing (years, days, hours, minutes).
        """

        years = int(star_distance_ly)  # Whole years as an integer
        fractional_years = star_distance_ly - years  # Fractional part of years

        # Convert fractional years to days with remainder (approximate)
        days = int(fractional_years * 365.25)  
        fractional_days = (fractional_years * 365.25) - days

        # Convert fractional days to hours with remainder(approximate)
        hours = int(fractional_days * 24)
        fractional_hours = (fractional_days * 24) - hours  

        # Convert fractional hours to minutes (approximate)
        minutes = int(fractional_hours * 60)

        return years, days, hours, minutes





