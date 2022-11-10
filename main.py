import serial
import time
import flask
from flask import request, jsonify

arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)

# Motor Requests
def moveForward():
    arduino.write(bytes("MOVE_F", 'utf-8'))

def moveBackward():
    arduino.write(bytes("MOVE_B", 'utf-8'))

def moveLeft():
    arduino.write(bytes("MOVE_L", 'utf-8'))

def moveRight():
    arduino.write(bytes("MOVE_R", 'utf-8'))

def stopMotor():
    arduino.write(bytes("STOP_M", 'utf-8'))

# Flask API
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>FarmBot API</h1>
<p>A work in progress API for FarmBot</p>'''

@app.route('/farmbot/status', methods=['GET'])
def status():
    return "OK and good to go!"

# INFO should return - HUM: val TEMP: val SOIL: val 
@app.route('/farmbot/sensorinfo', methods=['GET'])
def sensorinfo():
    arduino.write(bytes("INFO", 'utf-8'))
    time.sleep(1)
    data = arduino.readline()
    return data

app.run()

