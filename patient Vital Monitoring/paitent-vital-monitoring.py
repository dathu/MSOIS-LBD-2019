import time
import Adafruit_DHT
import RPi.GPIO as GPIO #to use GPIO pins for Sensor and actuators
import serial, time
import paho.mqtt.client as mqtt

ser = serial.Serial('/dev/ttyACM0', 9600)

# to use Raspberry Pi board pin numbers  
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# set up GPIO output channel
GPIO.setup(26,GPIO.IN)  


# Define Variables
MQTT_BROKER = "test.mosquitto.org"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "JNNCESDPJAN19"

    
    
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
        x = ser.readline()
        mqttc.publish(MQTT_TOPIC,x)



     

# Disconnect from MQTT_Broker
mqttc.disconnect()
