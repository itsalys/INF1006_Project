# pip3 install paho-mqtt
import paho.mqtt.publish as publish
import time

mqtt_broker = "192.168.10.141"
mqtt_username = "admin"
mqtt_pwd = "mqttbroker"
mqtt_topic = "test/topic2"

while True:
    test_data = input("Enter Test Data: ")
    publish.single(mqtt_topic, 
                   payload=test_data, 
                   retain=True,
                   hostname=mqtt_broker,
                   auth={"username": mqtt_username, "password": mqtt_pwd})
    print(f"Published to {mqtt_topic}: {test_data}")

client.loop_forever()