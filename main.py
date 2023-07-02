from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import json

app = Flask(__name__)

connection = sqlite3.connect('database.db')
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS sensors (id INTEGER PRIMARY KEY, sensor_id INTEGER,  temperature REAL, humidity REAL, pressure REAL, light_intensity REAL, motion_detected INTEGER, timestamp TEXT, latitude REAL, longitude REAL)')

# Read in json file 
traffic = json.load(open('fake_data.json'))
columns = ['sensor_id', 'temperature', 'humidity', 'pressure', 'light_intensity', 'motion_detected', 'timestamp', 'latitude', 'longitude']
for row in traffic:
    keys = tuple(row[c] for c in columns)
    cursor.execute('INSERT INTO sensors (sensor_id, temperature, humidity, pressure, light_intensity, motion_detected, timestamp, latitude, longitude) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', keys)
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

@app.route('/api/sensors/<int:sensor_id>', methods=['GET'])
def get_sensor(sensor_id):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM sensors WHERE sensor_id=?', (sensor_id,))
    sensor = cursor.fetchall()
    connection.close()
    return json.dumps(sensor)


#Query the average temperature for a given sensor
@app.route('/api/sensors/<int:sensor_id>/temperature', methods=['GET'])
def get_sensor_temperature(sensor_id):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT AVG(temperature) FROM sensors WHERE sensor_id=?', (sensor_id,))
    sensor = cursor.fetchall()
    connection.close()
    return json.dumps(sensor)

#Query the average humidity for a given sensor
@app.route('/api/sensors/<int:sensor_id>/humidity', methods=['GET'])
def get_sensor_humidity(sensor_id):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT AVG(humidity) FROM sensors WHERE sensor_id=?', (sensor_id,))
    sensor = cursor.fetchall()
    connection.close()
    return json.dumps(sensor)

#Query sensor data for a gievn date range
# TODO: this needs work to get the date range working properly.
@app.route('/api/sensors/<int:sensor_id>/date', methods=['GET'])
def get_sensor_date(sensor_id):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM sensors WHERE sensor_id=? AND timestamp BETWEEN ? AND ?', (sensor_id, request.args.get('start_date'), request.args.get('end_date')))
    sensor = cursor.fetchall()
    connection.close()
    return json.dumps(sensor)






if __name__ == '__main__':
    app.run(debug=True)
