#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 18:54:22 2024

@author: brendangallagher
"""


def find_closest_values(df, target_value):
    
    """
    Find the target value and the next closest value in a DataFrame column.
    
    Args:
    - df (DataFrame): The DataFrame containing the data.
    - target_value (float): The target value to find.
    
    Returns:
    - target_value (float): The value in the column closest to the target.
    - next_closest_value (float): The value in the column that is closest to 
    the target_value.
    """
    
    # Find index of closest value to the target value
    closest_index = (df['dist_ly'] - target_value).abs().idxmin()
    #closest_value = df['dist_ly'][closest_index]
    
    # We don't want the value itself, so drop and use the closes next closest
    df_excluded = df.drop(index=closest_index)
    next_closest_index = (df_excluded['dist_ly'] - target_value).abs().idxmin()
    next_closest_value = df_excluded['dist_ly'][next_closest_index]
    
    return next_closest_value