#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 19:55:55 2024

@author: brendangallagher
"""

from datetime import datetime

class AgeCalculator:
    @staticmethod
    def calculate_age(birthdate):
        today = datetime.today()
        age_delta = today - birthdate
        years = age_delta.days // 365
        days = age_delta.days % 365
        hours, remainder = divmod(age_delta.seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        return years, days, hours, minutes

    @staticmethod
    def calculate_light_age(star_distance_ly):
        years = int(star_distance_ly) 
        fractional_years = star_distance_ly - years
        days = int(fractional_years * 365.25)
        fractional_days = (fractional_years * 365.25) - days
        hours = int(fractional_days * 24)
        fractional_hours = (fractional_days * 24) - hours
        minutes = int(fractional_hours * 60)
        return years, days, hours, minutes