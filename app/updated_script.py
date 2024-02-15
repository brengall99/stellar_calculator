import csv
from datetime import datetime, timedelta

def calculate_age(birthdate):
    today = datetime.today()
    age_delta = today - birthdate
    years = age_delta.days // 365
    days = age_delta.days % 365
    hours, remainder = divmod(age_delta.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    return years, days, hours, minutes

def calculate_light_age(star_distance_ly):
    years = int(star_distance_ly) 
    fractional_years = star_distance_ly - years
    days = int(fractional_years * 365.25)
    fractional_days = (fractional_years * 365.25) - days
    hours = int(fractional_days * 24)
    fractional_hours = (fractional_days * 24) - hours
    minutes = int(fractional_hours * 60)

    return years, days, hours, minutes

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

def find_closest_star(age_years):
    closest_star = None
    closest_distance = float('inf')
    closest_constellation = None

    try:
        with open('data/star_data.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if 'dist_ly' in row:
                    try:
                        star_distance = float(row['dist_ly'])
                    except ValueError:
                        continue  # Skip this star if distance is not a valid number
                    distance = abs(age_years - star_distance)
                    if distance < closest_distance:
                        closest_star = row['proper'] if row['proper'] else row['gl']
                        closest_constellation = row['constellation']
                        closest_distance = star_distance  # Store the actual star distance
                        
    except FileNotFoundError:
        print("Star data file not found.")

    return closest_star, closest_distance, closest_constellation

def main():
    birthdate_str = "08-09-1999"
    try:
        birthdate = datetime.strptime(birthdate_str, "%d-%m-%Y")
    except ValueError:
        print("Invalid date format. Please use dd-mm-yyyy.")
        return
    
    age_years, age_days, age_hours, age_minutes = calculate_age(birthdate)
    
    closest_star, star_distance_ly, closest_constellation_iau = find_closest_star(age_years)
    
    light_age_years, light_age_days, light_age_hours, light_age_minutes = calculate_light_age(star_distance_ly)
    
    constellation_data = load_constellation_data()
    
    closest_constellation = constellation_data.get(closest_constellation_iau, closest_constellation_iau)

    print(f"\nYou are {age_years} years, {age_days} days, {age_hours} hours, and {age_minutes} minutes old.")
    if closest_star:
        print(f"The light from the star '{closest_star}' in the constellation {closest_constellation},")
        print(f"emitted approximately {light_age_years} years, {light_age_days} days, {light_age_hours} hours,")
        print(f"and {light_age_minutes} minutes ago.")
    else:
        print("No star data found.")

if __name__ == "__main__":
    main()
