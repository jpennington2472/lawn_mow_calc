from flask import Flask, jsonify, request, render_template, redirect
import csv
import pandas as pd

app = Flask(__name__)

# File to store collected data
data_file = "lawn_mowing_data.csv"

# Ensure the file exists
fields = ["Lawn Size", "Terrain Difficulty", "Grass Height", "Location Type", "Mowing Cost"]
try:
    with open(data_file, 'x', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(fields)
except FileExistsError:
    pass

# Function to read data from CSV
def load_data_from_csv(file_path):
    df = pd.read_csv(data_file)
    return df.to_dict(orient='records')

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/api/lawn_data', methods=['GET'])
def get_lawn_data():
    lawn_data = load_data_from_csv(data_file)
    return jsonify(lawn_data)

@app.route('/submit', methods=['POST'])
def submit():
    lawn_size = request.form['lawn_size']
    terrain = request.form['terrain']
    grass = request.form['grass']
    location = request.form['location']
    cost = request.form['cost']

    # Save to CSV
    with open(data_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([lawn_size, terrain, grass, location, cost])

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
