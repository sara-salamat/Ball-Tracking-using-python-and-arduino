import cv2
import numpy as np
import serial
import time
import sys

# specifying index of our video input
cam = cv2.VideoCapture(1)
kernelopen = np.ones((8,8))


lowerbound = np.array([10 , 150 , 0])
upperbound = np.array([32,255 ,255])

arduino = serial.Serial('COM9' , baudrate=9600)
time.sleep(2)

while True:
    retval , image = cam.read()
    image = cv2.resize(image , (300 , 300))
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    mask = cv2.inRange(image_hsv , lowerbound , upperbound)
    mask = cv2.morphologyEx(mask , cv2.MORPH_OPEN ,kernelopen )
    mask = cv2.morphologyEx(mask , cv2.MORPH_CLOSE ,np.ones((3,3)))
    cv2.imshow('masked image' ,mask)
    cv2.imshow('camera' ,image)
    M = cv2.moments(mask)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
    else:
        cX, cY = 0, 0

    print('x: {} y: {}'.format(cX , cY))
    data = "X{0:d}Y{1:d}Z".format(cX, cY)
    arduino.write(data.encode())
    cv2.waitKey(10)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
       break