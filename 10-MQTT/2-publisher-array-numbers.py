# Import package
import paho.mqtt.client as mqtt
import time

# Define Variables
MQTT_BROKER = "test.mosquitto.org"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "msois"


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


x = 1
num = 1

for num in range(1,20):
    print x
    num = x
    MQTT_MSG = num
    # Publish message to MQTT Topic 
    mqttc.publish(MQTT_TOPIC,MQTT_MSG)
    time.sleep(5)
    x= x + 1
    #if (x > 19):
     #   exit


     

# Disconnect from MQTT_Broker
mqttc.disconnect()





