# pip3 install paho-mqtt
import paho.mqtt.publish as publish
import time

mqtt_broker = "192.168.1.2"
mqtt_username = "admin"
mqtt_pwd = "mqttbroker"
mqtt_topic = "Doorway/MotionSensor"


publish.single(mqtt_topic, 
                payload="On", 
                retain=True,
                hostname=mqtt_broker,
                auth={"username": mqtt_username, "password": mqtt_pwd})
print("MotionSensor On")
