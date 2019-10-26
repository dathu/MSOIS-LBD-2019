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
MQTT_TOPIC = "jnncesdpjan"
MQTT_TOPIC1 = "soismanipal"

# Initialization for Soil Moisture Sensor
#GPIO SETUP
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
    
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
        
        # Temparature Sensor
        humidity, temperature = Adafruit_DHT.read_retry(22, 4) # Sensor,GPIO Pin
        print('Temp:{0:0.1f} C\n Humidity:{1:0.1f} %'.format(temperature, humidity))
        x = "Humidity "
        y = str(float(humidity))
        MQTT_MSG = x + y
        mqttc.publish(MQTT_TOPIC,MQTT_MSG)

        w = "Temperature "
        z = str(float(temperature))
        MQTT_MSG1 = w + z
        mqttc.publish(MQTT_TOPIC,MQTT_MSG1)

        # Soil Moisture
        a = GPIO.input(channel)
        print(a)
        if (a==0):
                print("------------------------------------")
                print("Soil is Wet (0)")
                f = "Soil is Wet (0):"
                g = str(int(a))
                MQTT_MSG2 = f + g
                mqttc.publish(MQTT_TOPIC1,MQTT_MSG2)
                print("Waiting for Sensor To Settle")
                time.sleep(2)
        else:
                print("------------------------------------")
                print("Soil is Dry (1)")
                h = "Soil is Dry (1):"
                i = str(int(a))
                MQTT_MSG3 = h + i
                mqttc.publish(MQTT_TOPIC1,MQTT_MSG3)
                print("Waiting for Sensor To Settle")
                time.sleep(2)

        time.sleep(5)
     

# Disconnect from MQTT_Broker
mqttc.disconnect()
