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
    # define range of blue color in HSV
    lower_red = np.array([0,100,20])
    upper_red = np.array([10,255,255])

    # lower boundary RED color range values; Hue (0 - 10)
    lower1 = np.array([0, 100, 20])
    upper1 = np.array([10, 255, 255])
 
# upper boundary RED color range values; Hue (160 - 180)
    lower2 = np.array([160,100,20])
    upper2 = np.array([179,255,255])
    # Threshold the HSV image to get only blue colors
    lower_mask = cv.inRange(hsv, lower1, upper1)
    upper_mask = cv.inRange(hsv, lower2, upper2)
 
    full_mask = lower_mask + upper_mask

    #mask = cv.inRange(hsv, lower_red, upper_red)

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
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv.imshow('frame', frame)

    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

    #cv.imshow('frame',frame)
    #cv.imshow('mask',mask)
    #cv.imshow('res',res)

cv.destroyAllWindows()