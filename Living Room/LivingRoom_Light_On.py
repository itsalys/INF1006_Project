# pip3 install paho-mqtt
import paho.mqtt.publish as publish
import time
from gpiozero import LED

mqtt_broker = "192.168.1.3"
mqtt_username = "admin"
mqtt_pwd = "mqttbroker"
mqtt_topic = "LivingRoom/Light"


publish.single(mqtt_topic, 
                payload="On", 
                retain=True,
                hostname=mqtt_broker,
                auth={"username": mqtt_username, "password": mqtt_pwd})
print("Light On")
led = LED()
led.on()
