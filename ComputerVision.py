# Computer Vision Project 1 - Colour Detection

# Project imports
import cv2
import numpy as np

# Set ranges for HSV 
lower = np.array([15, 150, 30])
upper = np.array([24, 255, 255])

# Gets webcam footage 
video = cv2.VideoCapture(0)

# Runs program on a loop 
while True:

    # Reads webcam footage
    success, img = video.read()

    # Converts BGR to HSV 
    image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Finding contours in mask image
    mask = cv2.inRange(image, lower, upper)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Finds position of all contours 
    if len(contours) != 0:
        for contour in contours:
            if cv2.contourArea(contour) > 500:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(img, (x,y), (x + w, y +h), (0, 0, 255), 3)  

    # Display mask image
    cv2.imshow("mask", mask)

    # Display webcam footage
    cv2.imshow("webcam", img)

    cv2.waitKey(1)

    