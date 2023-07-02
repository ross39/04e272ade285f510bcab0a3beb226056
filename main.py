from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import json

app = Flask(__name__)

connection = sqlite3.connect('database.db')
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS sensors (id INTEGER PRIMARY KEY, temperature REAL, humidity REAL, pressure REAL, light_intensity REAL, motion_detected INTEGER, timestamp TEXT, latitude REAL, longitude REAL)')

# Read in json file 
traffic = json.load(open('fake_data.json'))
columns = ['temperature', 'humidity', 'pressure', 'light_intensity', 'motion_detected', 'timestamp', 'latitude', 'longitude']
for row in traffic:
    keys = tuple(row[c] for c in columns)
    cursor.execute('INSERT INTO sensors (temperature, humidity, pressure, light_intensity, motion_detected, timestamp, latitude, longitude) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', keys)
    print('Inserted row:', keys)

connection.commit()
connection.close()





@app.route('/')
def home_page():
    return 'welcome to the home page!'

# Define rest endpoint
@app.route('/api', methods=['GET', 'POST'])
def api_page():
    if request.method == 'GET':
        return 'You are using GET'
    elif request.method == 'POST':
        return 'You are using POST'
    else:
        return 'Invalid request'

@app.route('/api/sensors', methods=['GET'])
def get_sensors():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM sensors')
    sensors = cursor.fetchall()
    connection.close()
    return json.dumps(sensors)




if __name__ == '__main__':
    app.run(debug=True)
