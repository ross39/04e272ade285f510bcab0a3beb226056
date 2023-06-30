from flask import Flask, jsonify, request
import random


app = Flask(__name__)

# Create mock data to show off our api 
# (this would normally be data from a database)
sensor_one_data = {
    'sensor_id': 1,
    'sensor_name': 'Sensor One',
    'temperature': random.randint(0, 100),
    'humidity': random.randint(0, 100)
}

sensor_two_data = {
    'sensor_id': 2,
    'sensor_name': 'Sensor One',
    'temperature': random.randint(0, 100),
    'humidity': random.randint(0, 100)
}





@app.route('/')
def home_page():
    return 'Welcome to the home page!'

# Define rest endpoint
@app.route('/api', methods=['GET', 'POST'])
def api_page():
    if request.method == 'GET':
        return 'You are using GET'
    elif request.method == 'POST':
        return 'You are using POST'
    else:
        return 'Invalid request'

@app.route('/api/sensor_one', methods=['GET'])
def sensor_one():
    return jsonify(sensor_one_data)

@app.route('/api/sensor_two', methods=['GET'])
def sensor_two():
    return jsonify(sensor_two_data)

@app.route('/api/all_sensors', methods=['GET'])
def all_sensors():
    # Return the result of multiple api calls
    return jsonify([sensor_one_data, sensor_two_data])

@app.route('/api/sensor_one/average_temperature', methods=['GET'])
def sensor_one_average_temperature():
    # Return the average temperature of sensor one
    return jsonify(sensor_one_data['temperature'])

@app.route('/api/sensor_two/average_temperature', methods=['GET'])
def sensor_two_average_temperature():
    # Return the average temperature of sensor two
    return jsonify(sensor_two_data['temperature'])

@app.route('/api/all_sensors/average_temperature', methods=['GET'])
def all_sensors_average_temperature():
    # Return the average temperature of all sensors
    return jsonify((sensor_one_data['temperature'] + sensor_two_data['temperature']) / 2)

