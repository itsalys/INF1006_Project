# pip3 install paho-mqtt
import paho.mqtt.client as mqtt 

mqtt_broker = "192.168.10.141"
mqtt_username = "admin"
mqtt_pwd = "mqttbroker"

# The callback function. It will be triggered when trying to connect to the MQTT broker
# client is the client instance connected this time
# userdata is users' information, usually empty. If it is needed, you can set it through user_data_set function.
# flags save the dictionary of broker response flag.
# rc is the response code.
# Generally, we only need to pay attention to whether the response code is 0.
def on_connect(client, userdata, flags, rc):
    print("Connection attempt returned: " + mqtt.connack_string(rc))
    print(f"Successfully connected to MQTT Broker @ {mqtt_broker}")

client = mqtt.Client() 
client.username_pw_set(mqtt_username, mqtt_pwd)
client.on_connect = on_connect 
client.connect(mqtt_broker, 1883) 
client.loop_forever()