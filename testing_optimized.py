
import cv2
import numpy as np

# Create the face recognizer and load the trained model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('C:\Users\srina\OneDrive\Desktop\vscode\fams\TrainingImageLabel\trainer.yml')

# Load the Haar Cascade for face detection
cascadePath = "C:\Users\srina\OneDrive\Desktop\vscode\fams\haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

# Set the font for displaying text
font = cv2.FONT_HERSHEY_SIMPLEX

# Start video capture
cam = cv2.VideoCapture(0)

try:
    while True:
        ret, im = cam.read()
        if not ret:
            print("Failed to capture image")
            break

        # Convert the image to grayscale
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = faceCascade.detectMultiScale(gray, 1.1, 5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            # Predict the ID of the detected face
            Id, conf = recognizer.predict(gray[y:y+h, x:x+w])

            # Confidence threshold for recognition
            if conf < 100:  # You can adjust this threshold
                Id_text = f"ID: {Id} (Confidence: {conf:.2f})"
                color = (0, 255, 0)  # Green for recognized faces
            else:
                Id_text = "Unknown"
                color = (0, 0, 255)  # Red for unknown faces

            # Draw a rectangle around the face
            cv2.rectangle(im, (x, y), (x + w, y + h), color, 2)
            # Put the ID text above the rectangle
            cv2.putText(im, Id_text, (x, y - 10), font, 0.8, color, 2)

        # Display the resulting frame
        cv2.imshow('Face Recognition', im)

        # Break the loop on 'q' key press
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Exiting...")

finally:
    # Release the video capture and destroy all windows
    cam.release()
    cv2.destroyAllWindows()
