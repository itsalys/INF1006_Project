
import cv2

# Set up the face detection classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize the video capture
video_capture = cv2.VideoCapture(0)

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
        cv2.imwrite('face_detected.jpg', frame)
        print("Image saved!")

        break

    # Display the frame without face detections
    cv2.imshow('Face Detection', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture resources
video_capture.release()

# Destroy all OpenCV windows
cv2.destroyAllWindows()
