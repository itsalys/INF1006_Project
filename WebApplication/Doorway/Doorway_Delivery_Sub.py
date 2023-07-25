# pip3 install paho-mqtt
import paho.mqtt.client as mqtt
import base64
import io
from PIL import Image

mqtt_broker = "192.168.1.2"
mqtt_username = "admin"
mqtt_pwd = "mqttbroker"
topics = [("Doorway/UltrasonicSensor", 0), ("Doorway/DeliveryCamera", 0), ("Doorway/SecurityCamera", 0)]

def on_connect(client, userdata, flags, rc):
    print("Connection attempt returned: " + mqtt.connack_string(rc))
    print(f"Successfully connected to MQTT Broker @ {mqtt_broker}")

# runs whenever a new msg is received from mqtt broker
def on_message(client, userdata, msg):
    print(f"{msg.topic}: {msg.payload.decode()}\n")
    
    if msg.topic == "Doorway/UltrasonicSensor":
        if msg.payload.decode() == "In Range":
            # Delivery
            print("Delivery")
            
        if msg.payload.decode() == "Out of Range":
            # No Delivery 
            print("No Delivery")
        
    if msg.topic == "Doorway/DeliveryCamera":
        # Display Picture On Screen
        print("Picture !")
        image_data = base64.b64decode(msg.payload)
    
        # Create an image object from the decoded data
        image = Image.open(io.BytesIO(image_data))
        
        # Save the image to a file
        image.save("Delivery_image.jpg")
        
        print("Image saved successfully.")
        
    if msg.topic == "Doorway/SecurityCamera":
        # Person Detected Notification
        
        # Display Picture On Screen
        print("Picture !")
        image_data = base64.b64decode(msg.payload)
    
        # Create an image object from the decoded data
        image = Image.open(io.BytesIO(image_data))
        
        # Save the image to a file
        image.save("Security_image.jpg")
        
        print("Image saved successfully.")
        

client = mqtt.Client()
client.username_pw_set(mqtt_username, mqtt_pwd) # comment out if no usr name and password set
client.connect(mqtt_broker, 1883)
client.on_connect = on_connect
client.subscribe(topics)
client.on_message = on_message
client.loop_forever()