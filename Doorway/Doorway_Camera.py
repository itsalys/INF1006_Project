#from picamera import PiCamera
from time import sleep
import paho.mqtt.client as mqtt
import base64
import paho.mqtt.publish as publish

# camera = PiCamera()
# camera.start_preview()
# camera.start_recording('/home/pi/Desktop/video.h264')
# sleep(5)
# camera.stop_recording()
# camera.stop_preview()


mqtt_broker = "192.168.1.2"
mqtt_username = "admin"
mqtt_pwd = "mqttbroker"
mqtt_topic = "Doorway/Camera"

# Read the image file
image_path = 'C:/Users/clari/Desktop/yelan.jpg'
with open(image_path, "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

# Create MQTT client
client = mqtt.Client()

publish.single(mqtt_topic, 
                payload=encoded_image, 
                retain=True,
                hostname=mqtt_broker,
                auth={"username": mqtt_username, "password": mqtt_pwd})

# Connect to the MQTT broker
client.connect(mqtt_broker, 1883) 

# Publish the image to the MQTT broker
client.publish(mqtt_topic, encoded_image)
print("here")

# Disconnect from the MQTT broker
client.disconnect()
