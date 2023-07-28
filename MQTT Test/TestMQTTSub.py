# pip3 install paho-mqtt
import paho.mqtt.client as mqtt

mqtt_broker = "192.168.1.2"
mqtt_username = "admin"
mqtt_pwd = "mqttbroker"
topics = [("Doorway/Delivery", 0), ("Doorway/Security", 0)]

def on_connect(client, userdata, flags, rc):
    print("Connection attempt returned: " + mqtt.connack_string(rc))
    print(f"Successfully connected to MQTT Broker @ {mqtt_broker}")

# runs whenever a new msg is received from mqtt broker
def on_message(client, userdata, msg):
    print(f"{msg.topic}\n")

client = mqtt.Client()
client.username_pw_set(mqtt_username, mqtt_pwd) # comment out if no usr name and password set
client.connect(mqtt_broker, 1883)
client.on_connect = on_connect
client.subscribe(topics)
client.on_message = on_message
client.loop_forever()