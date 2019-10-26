import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO  
import time

# Define Variables
MQTT_BROKER = "test.mosquitto.org"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "jnncesubsdp"

#uresponce

# to use Raspberry Pi board pin numbers  
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# set up GPIO output channel
GPIO.setup(21,GPIO.OUT)  

# Define on_connect epent Handler
def on_connect(mosq, obj, rc):
	#Subscribe to a the Topic
	mqttc.subscribe(MQTT_TOPIC, 0)

# Define on_subscribe event Handler
def on_subscribe(mosq, obj, mid, granted_qos):
    print "Subscribed to MQTT Topic"

# Define on_message event Handler
def on_message(mosq, obj, msg):
        print msg.payload
        uresponce = msg.payload
        if (uresponce == "ON"):
                GPIO.output(21,GPIO.HIGH)
        if (uresponce == "OFF"):
                GPIO.output(21,GPIO.LOW)


# Initiate MQTT Client
mqttc = mqtt.Client()

# Register Event Handlers
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

# Connect with MQTT Broker
mqttc.connect(MQTT_BROKER, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL )

# Continue the network loop
mqttc.loop_forever()
