# pip3 install paho-mqtt
import paho.mqtt.client as mqtt
import time

mqtt_broker = "192.168.10.141"
mqtt_username = "admin"
mqtt_pwd = "mqttbroker"
topic = "test/topic1"
test_data = "speak now releases this friday !"

def on_connect(client, userdata, flags, rc):
    print("Connection attempt returned: " + mqtt.connack_string(rc))
    print(f"Successfully connected to MQTT Broker @ {mqtt_broker}")

    client.publish(topic, payload=test_data, qos=0, retain=True)
    print(f"Published to {topic}: {test_data}")

client = mqtt.Client()
client.username_pw_set(mqtt_username, mqtt_pwd) # comment out if nvr set password
client.on_connect = on_connect
client.connect(mqtt_broker, 1883, 60)

client.loop_forever()