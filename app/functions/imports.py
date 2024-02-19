#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 07:59:42 2024

@author: brendangallagher
"""

import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from functions.myplot import load_and_prepare_data, plot_stars
from functions.age_calculator import AgeCalculator
from functions.star_data_handler import star_data_finder
from functions.distance_utils import find_star_by_distance, find_closest_values
from functions.constellation_loader import load_constellation_data
from functions.utils import validate_birthdate
import pandas as pd