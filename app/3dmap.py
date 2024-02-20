
# --- import libraries --- #

import pandas as pd  # data manipulation and analysis
import numpy as np  # numerical operations
import matplotlib.pyplot as plt  # plotting and visualisations
from mpl_toolkits.mplot3d import Axes3D  # 3D plotting toolkit


# --- functions --- #

def load_star_data(file_path): # load csv

    """
    Loads star data from a CSV file into a pandas DataFrame

    Args:
        file_path: directory for the data file

    Returns:
        file: the CSV file 
  """

  return pd.read_csv(file_path)  # Read the CSV file using pandas


def celestial_to_cartesian(ra_hours, dec_degrees, distance_ly):

    """
    Converts celestial coordinates (RA, Dec, Distance) to Cartesian (x, y, z).

    Args: 
        float: ra_hours
        float: dec_degrees
        float: distance_ly

    Returns:
        float: x, y, z
  """

  # convert RA from hours to degrees
  ra_degrees = ra_hours * 15

  # convert RA and Dec to radians for trigcalculations
  ra_rad = np.radians(ra_degrees)
  dec_rad = np.radians(dec_degrees)

  # calculate Cartesian coordinates using spherical trig
  x = distance_ly * np.cos(dec_rad) * np.cos(ra_rad)
  y = distance_ly * np.cos(dec_rad) * np.sin(ra_rad)
  z = distance_ly * np.sin(dec_rad)

  return x, y, z


# --- Main Script --- #

file_path = 'data/star_data.csv'  # load the star data
star_data = load_star_data(file_path)  # invoke function

# exclude Polaris from the data and filter based on 'proper' column
star_data = star_data[star_data['proper'] != 'Polaris'] 

# convert celestial coordinates to cartesian
star_data['x'], star_data['y'], star_data['z'] = celestial_to_cartesian(
  star_data['ra'], star_data['dec'], star_data['dist_ly'])

# create a 3D scatter plot
fig = plt.figure(figsize=(10, 10))  # create figure
ax = fig.add_subplot(111, projection='3d')  # add 3D subplot

# plot the stars as black dots without gridlines
ax.scatter(star_data['x'], star_data['y'], star_data['z'],\
c='black', marker='.')
ax.grid(False)

# set title and labels for the plot
plt.title('3D Star Map (Excluding Polaris)')
ax.set_xlabel('x (light-years)')
ax.set_ylabel('y (light-years)')
ax.set_zlabel('z (light-years)')

plt.show()  # display the plot
