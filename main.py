from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import sqlite3
import json
import datetime
from invalid_usage import InvalidUsage

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


def toDate(dateString): 
    return datetime.datetime.strptime(dateString, "%Y-%m-%d").date()



@app.route('/')
def home_page():
    return 'welcome to the home page!'

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

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
    # Try and execute the query and if it fails, return http error 400
    try:
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM sensors')
        sensors = cursor.fetchall()
        connection.close()
        return json.dumps(sensors)
    except ValueError:
        raise InvalidUsage(400)
    

@app.route('/api/sensors/<int:sensor_id>', methods=['GET'])
def get_sensor(sensor_id):
    try:
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM sensors WHERE sensor_id=?', (sensor_id,))
        sensor = cursor.fetchall()
        connection.close()
        return json.dumps(sensor)
    except ValueError:
        return InvalidUsage(400)

#Query the average temperature for a given sensor
@app.route('/api/sensors/<int:sensor_id>/temperature', methods=['GET'])
def get_sensor_temperature(sensor_id):
    try:
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute('SELECT AVG(temperature) FROM sensors WHERE sensor_id=?', (sensor_id,))
        sensor = cursor.fetchall()
        connection.close()
        return json.dumps(sensor)
    except ValueError:
        return InvalidUsage(400)

#Query the average humidity for a given sensor
@app.route('/api/sensors/<int:sensor_id>/humidity', methods=['GET'])
def get_sensor_humidity(sensor_id):
    try:
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute('SELECT AVG(humidity) FROM sensors WHERE sensor_id=?', (sensor_id,))
        sensor = cursor.fetchall()
        connection.close()
        return json.dumps(sensor)
    except ValueError:
        return InvalidUsage(400)
    
#Query all data for a given sensor between now and a given date
@app.route('/api/sensors/<int:sensor_id>/data/<string:date>', methods=['GET'])
def get_sensor_data(sensor_id, date):
    try:
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM sensors WHERE sensor_id=? AND timestamp BETWEEN ? AND ?', (sensor_id, date, datetime.datetime.now()))
        sensor = cursor.fetchall()
        connection.close()
        return json.dumps(sensor)
    except ValueError:
        return InvalidUsage(400)
#Query average temperature for a given sensor between now and a given date
@app.route('/api/sensors/<int:sensor_id>/temperature/<string:date>', methods=['GET'])
def get_sensor_temperature_date(sensor_id, date):
    try:
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute('SELECT AVG(temperature) FROM sensors WHERE sensor_id=? AND timestamp BETWEEN ? AND ?', (sensor_id, date, datetime.datetime.now()))
        sensor = cursor.fetchall()
        connection.close()
        return json.dumps(sensor)
    except ValueError:
        return InvalidUsage(400)

#Query average humidity for a given sensor between now and a given date. Throw an exception if the format is not correct
@app.route('/api/sensors/<int:sensor_id>/humidity/<string:date>', methods=['GET'])
def get_sensor_humidity_date(sensor_id, date):
    try:
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute('SELECT AVG(humidity) FROM sensors WHERE sensor_id=? AND timestamp BETWEEN ? AND ?', (sensor_id, date, datetime.datetime.now()))
        sensor = cursor.fetchall()
        connection.close()
        return json.dumps(sensor)
    except ValueError:
        return InvalidUsage(400)
    

  

  






if __name__ == '__main__':
    app.run(debug=True)
