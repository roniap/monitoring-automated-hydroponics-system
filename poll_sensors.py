import RPi.GPIO as GPIO
import dht11
import time
import datetime

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 17
instance = dht11.DHT11(pin=17)

def poll():
    result = instance.read()
    if result.is_valid():
        return {
          "Last Record": int(time.time()), 
          "Temperature: %d C": % result.temperature, 
          "Temperature: %d F" % ((result.temperature * 9/5) + 32)
          "Humidity": result.humidity
        }
