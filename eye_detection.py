import sys
import cv2

# Load the Haar cascades for eyes
eye_cascade = cv2.CascadeClassifier("C:/Users/cheer/OneDrive/Desktop/haarcascade_eye.xml")
car_cascade = cv2.CascadeClassifier("C:/Users/cheer/Downloads/haarcascade_car.xml")

# Check if the Haar cascade was successfully loaded
if eye_cascade.empty():
    print("Error: Could not load Haar cascade file.")
    exit()

# Parse the command line arguments
# Ask the user to choose the input option
option = input("Choose input option (1 = image file, 2 = camera): ")

# If the option is 'camera', use the system camera
if option == "2":
    # Create a VideoCapture object to capture frames from the camera
    cap = cv2.VideoCapture(0)

    # Check if the camera was successfully opened
    if not cap.isOpened():
        print("Error: Could not open camera.")
        exit()

    while True:
        # Capture a frame from the camera
        ret, frame = cap.read()

        # Check if the frame was successfully captured
        if not ret:
            print("Error: Could not capture frame.")
            break

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect eyes in the frame
        eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        cars = car_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)



        # Draw rectangles around the detected eyes
        for (x, y, w, h) in eyes:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        for (x, y, w, h) in cars:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # Display the frame with the detected eyes
        cv2.imshow('frame', frame)

        # Wait for a key press
        key = cv2.waitKey(1)

        # If the 'q' key is pressed, exit the loop
        if key == ord('q'):
            break

    # Release the VideoCapture object and destroy all windows
    cap.release()
    cv2.destroyAllWindows()

# If the option is an image file, load the image and detect eyes
else:
    # Ask the user to enter the file path
    file_path = input("Enter the file path: ")

    # Load the input image file
    img = cv2.imread(file_path)

    # Check if the image was successfully loaded
    if img is None:
        print("Error: Could not load image file.")
        exit()

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect eyes in the image
    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Draw rectangles around the detected eyes
    for (x, y, w, h) in eyes:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the image with the detected eyes
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
