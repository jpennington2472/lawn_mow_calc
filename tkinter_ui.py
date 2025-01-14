import tkinter as tk
from tkinter import messagebox
import csv

# File to store collected data
data_file = "lawn_mowing_data.csv"

# Create the file if it doesn't exist
fields = ["Lawn Size", "Terrain Difficulty", "Grass Height", "Location Type", "Mowing Cost"]
try:
    with open(data_file, 'x', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(fields)
except FileExistsError:
    pass

def save_data():
    lawn_size = entry_lawn_size.get()
    terrain = entry_terrain.get()
    grass = entry_grass.get()
    location = entry_location.get()
    cost = entry_cost.get()

    # Validate inputs
    if not all([lawn_size, terrain, grass, location, cost]):
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    # Save data
    with open(data_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([lawn_size, terrain, grass, location, cost])

    messagebox.showinfo("Success", "Data saved successfully!")
    clear_entries()

def clear_entries():
    entry_lawn_size.delete(0, tk.END)
    entry_terrain.delete(0, tk.END)
    entry_grass.delete(0, tk.END)
    entry_location.delete(0, tk.END)
    entry_cost.delete(0, tk.END)

# Create the Tkinter window
root = tk.Tk()
root.title("Lawn Mowing Data Collection")

# Add input fields
tk.Label(root, text="Lawn Size (sq ft):").grid(row=0, column=0)
entry_lawn_size = tk.Entry(root)
entry_lawn_size.grid(row=0, column=1)

tk.Label(root, text="Terrain Difficulty (1=Easy, 2=Moderate, 3=Hard):").grid(row=1, column=0)
entry_terrain = tk.Entry(root)
entry_terrain.grid(row=1, column=1)

tk.Label(root, text="Grass Height (1=Short, 2=Medium, 3=Tall):").grid(row=2, column=0)
entry_grass = tk.Entry(root)
entry_grass.grid(row=2, column=1)

tk.Label(root, text="Location Type (1=Urban, 2=Suburban, 3=Rural):").grid(row=3, column=0)
entry_location = tk.Entry(root)
entry_location.grid(row=3, column=1)

tk.Label(root, text="Mowing Cost ($):").grid(row=4, column=0)
entry_cost = tk.Entry(root)
entry_cost.grid(row=4, column=1)

# Add buttons
tk.Button(root, text="Save", command=save_data).grid(row=5, column=0, pady=10)
tk.Button(root, text="Clear", command=clear_entries).grid(row=5, column=1, pady=10)

# Run the application
root.mainloop()
