from gpiozero import DistanceSensor
from picamera import PiCamera
from time import sleep
import paho.mqtt.client as mqtt
import base64
import paho.mqtt.publish as publish


camera = PiCamera()
image_path="image.jpg"
mqtt_broker = "192.168.1.2"
mqtt_username = "admin"
mqtt_pwd = "mqttbroker"
mqtt_topic = "Doorway/Camera"

sleep(2)

ultrasonic = DistanceSensor(echo=17, trigger=4, threshold_distance=0.1)

def hello():
    print("Hello")
def bye():
    print("Bye")


while True:
    #in range
    ultrasonic.wait_for_in_range()
    print("In range")
    # Capture an image
    camera.capture('image.jpg')
    # Close the camera instance
    camera.close()
    ultrasonic.when_in_range = hello()
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
    print("encode: ", encoded_image)
    # Disconnect from the MQTT broker
    client.disconnect()

    
    #out of range
    ultrasonic.wait_for_out_of_range()
    print("Out of range")
    #nth
    ultrasonic.when_out_of_range = bye()

