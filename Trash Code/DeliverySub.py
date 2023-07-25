from gpiozero import DistanceSensor
from picamera import PiCamera
import base64
import paho.mqtt.publish as publish
from time import sleep

mqtt_broker = "192.168.1.2"
mqtt_username = "admin"
mqtt_pwd = "mqttbroker"

camera = PiCamera()
image_path="image.jpg"

sleep(2)

ultrasonic = DistanceSensor(echo=17, trigger=4, threshold_distance=0.1)

def hello():
    print("Hello")
    publish.single("Doorway/UltrasonicSensor", 
                   payload="In Range", 
                   retain=True,
                   hostname=mqtt_broker,
                   auth={"username": mqtt_username, "password": mqtt_pwd})
    print(f"Published to Doorway/UltrasonicSensor: In Range")

    camera.capture('image.jpg')
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

    publish.single("Doorway/DeliveryCamera", 
                    payload=encoded_image, 
                    retain=True,
                    hostname=mqtt_broker,
                    auth={"username": mqtt_username, "password": mqtt_pwd})

def bye():
    print("Bye")
    publish.single("Doorway/UltrasonicSensor", 
                   payload="Out of Range", 
                   retain=True,
                   hostname=mqtt_broker,
                   auth={"username": mqtt_username, "password": mqtt_pwd})
    print(f"Published to Doorway/UltrasonicSensor: Out of Range")


while True:
    ultrasonic.wait_for_in_range()
    print("In range")
    ultrasonic.when_in_range = hello()
    
    ultrasonic.wait_for_out_of_range()
    print("Out of range")
    ultrasonic.when_out_of_range = bye()