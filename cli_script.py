import csv
import os

# File to store collected data
data_file = "lawn_mowing_data.csv"

# Define the fields for data collection
fields = ["lawn_size", "terrain_difficulty", "grass_height", "location_type", "mowing_cost"]

# Create the file if it doesn't exist
if not os.path.exists(data_file):
    with open(data_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(fields)

def collect_data():
    print("\n=== Lawn Mowing Data Collection ===")
    
    # Collect data inputs
    lawn_size = input("Enter lawn size (sq ft): ")
    terrain_difficulty = input("Enter terrain difficulty (1=Easy, 2=Moderate, 3=Hard): ")
    grass_height = input("Enter grass height (1=Short, 2=Medium, 3=Tall): ")
    location_type = input("Enter location type (1=Urban, 2=Suburban, 3=Rural): ")
    mowing_cost = input("Enter mowing cost ($): ")
    
    # Append the data to the CSV file
    with open(data_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([lawn_size, terrain_difficulty, grass_height, location_type, mowing_cost])
    
    print("Data saved successfully!")

# Main loop for data collection
while True:
    collect_data()
    another = input("Would you like to enter another record? (yes/no): ").strip().lower()
    if another != "yes":
        print("\nData collection complete! Saved in 'lawn_mowing_data.csv'")
        break
