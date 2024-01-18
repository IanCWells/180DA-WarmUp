#References
#https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html

#for calibrating a proper red coloration
#https://cvexplained.wordpress.com/2020/04/28/color-detection-hsv/#:~:text=The%20HSV%20values%20for%20true,10%20and%20160%20to%20180.

import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of green color in HSV
    HSV: (99, 213, 219)
    lower_green = np.array([70,150,150])
    upper_green = np.array([130,255,255])
 
    # Threshold the HSV image to get only blue colors
    full_mask = cv.inRange(hsv, lower_green, upper_green)

    # Adaptive thresholding
    _, thresh = cv.threshold(full_mask, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

    # Find contours
    contours, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # Check if contours are found
    if contours:
        # Sort contours based on area (largest to smallest)
        contours = sorted(contours, key=cv.contourArea, reverse=True)

        # Get the largest contour
        largest_contour = contours[0]

        # Get bounding box coordinates
        x, y, w, h = cv.boundingRect(largest_contour)

        # Draw the bounding box on the original image
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv.imshow('frame', frame)

    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

    #cv.imshow('frame',frame)
    #cv.imshow('mask',mask)
    #cv.imshow('res',res)

cv.destroyAllWindows()