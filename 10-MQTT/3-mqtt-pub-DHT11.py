import time
import Adafruit_DHT
#import os # to execte relay script
import RPi.GPIO as GPIO #to use GPIO pins for Sensor and actuators
import serial, time
import paho.mqtt.client as mqtt


# Define Variables
MQTT_BROKER = "test.mosquitto.org"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "jnncesdp"

    
    
# Define on_connect event Handler
def on_connect(mosq, obj, rc):
	print "Connected to MQTT Broker"

# Define on_publish event Handler
def on_publish(client, userdata, mid):
	print "Message Published..."

# Initiate MQTT Client
mqttc = mqtt.Client()

# Register Event Handlers
mqttc.on_publish = on_publish
mqttc.on_connect = on_connect

# Connect with MQTT Broker
mqttc.connect(MQTT_BROKER, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL) 



while(1):
    humidity, temperature = Adafruit_DHT.read_retry(11, 4) # Sensor,GPIO Pin
    print('Temp:{0:0.1f} C\n Humidity:{1:0.1f} %'.format(temperature, humidity))
    x = "Humidity "
    y = str(float(humidity))
    MQTT_MSG = x + y
    mqttc.publish(MQTT_TOPIC,MQTT_MSG)

    w = "Temperature "
    z = str(float(temperature))
    MQTT_MSG1 = w + z
    mqttc.publish(MQTT_TOPIC,MQTT_MSG1)

    
    time.sleep(5)
     

# Disconnect from MQTT_Broker
mqttc.disconnect()
