# pip3 install paho-mqtt
import paho.mqtt.client as mqtt

# Raspi Imports
import RPi.GPIO as GPIO
import time

# mqtt_broker = "192.168.1.2"
mqtt_broker = "192.168.10.20" # Home Test
mqtt_username = "admin"
mqtt_pwd = "mqttbroker"
topics = [("LivingRoom/Light", 0), ("LivingRoom/Fan", 0)]

# LED & Step Motor Set up
LED = 16 # PIN16 = GPIO23
FAN = 18 # PIN18 = GPIO24
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)         # output pin
GPIO.setup(FAN, GPIO.OUT)         # output pin


def on_connect(client, userdata, flags, rc):
    print("Connection attempt returned: " + mqtt.connack_string(rc))
    print(f"Successfully connected to MQTT Broker @ {mqtt_broker}")

# runs whenever a new msg is received from mqtt broker
def on_message(client, userdata, msg):
    print(f"{msg.topic}: {msg.payload.decode()}\n")

    if(msg.topic == "LivingRoom/Light"): 
        if( msg.payload.decode() == "On"): GPIO.output(LED, 1) # Turn ON LED
        if( msg.payload.decode() == "Off"): GPIO.output(LED, 0) # Turn OFF LED

    if(msg.topic == "LivingRoom/Fan"): 
        if( msg.payload.decode() == "On"): GPIO.output(FAN, 1) # Turn ON FAN
        if( msg.payload.decode() == "Off"): GPIO.output(FAN, 0) # Turn OFF FAN

client = mqtt.Client()
client.username_pw_set(mqtt_username, mqtt_pwd) # comment out if no usr name and password set
client.connect(mqtt_broker, 1883)
client.on_connect = on_connect
client.subscribe(topics)
client.on_message = on_message
client.loop_forever()