# pip3 install paho-mqtt
import paho.mqtt.publish as publish
import time

mqtt_broker = "192.168.1.3"
mqtt_username = "admin"
mqtt_pwd = "mqttbroker"
mqtt_topic = "BabyRoom/VoiceSensor"


publish.single(mqtt_topic, 
                payload="Off", 
                retain=True,
                hostname=mqtt_broker,
                auth={"username": mqtt_username, "password": mqtt_pwd})
print("VoiceSensor Off")
