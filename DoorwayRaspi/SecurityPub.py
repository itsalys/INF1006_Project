from picamera import PiCamera
from time import sleep
import paho.mqtt.client as mqtt
import base64
import paho.mqtt.publish as publish
import cv2

# camera = PiCamera()
# camera.start_preview()
# camera.start_recording('/home/pi/Desktop/video.h264')
# sleep(5)
# camera.stop_recording()
# camera.stop_preview()

mqtt_broker = "192.168.1.2"
mqtt_username = "admin"
mqtt_pwd = "mqttbroker"
mqtt_topic = "Doorway/SecurityCamera"



import cv2

# Set up the face detection classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize the video capture
video_capture = cv2.VideoCapture(0)
while True:
    # Continuously capture frames from the camera
    while True:
        # Read a frame from the video capture
        ret, frame = video_capture.read()

        # Convert the captured frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Check if any faces are detected
        if len(faces) > 0:
            # Draw rectangles around the detected faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # Display the frame with face detections
            cv2.imshow('Face Detection', frame)

            # Save the image if a face is detected
            cv2.imwrite('/home/pi/Desktop/face.jpg', frame)
            print("Image saved!")

            break

        # Display the frame without face detections
        cv2.imshow('Face Detection', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture resources
    #video_capture.release()

    # Destroy all OpenCV windows
    cv2.destroyAllWindows()

    # Read the image file
    image_path = '/home/pi/Desktop/face.jpg'
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
    
    sleep(5)

    # Disconnect from the MQTT broker
    client.disconnect()

