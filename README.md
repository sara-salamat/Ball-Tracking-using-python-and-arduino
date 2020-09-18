# Ball-Tracking-using-python-and-arduino

In this project, I tried to control a servo motor to track a ping-pong ball. 

## python code

I used openCV and created a mask to filter the input video and detect regions of interest. then the masked image is enhanced using morphological operations and centroid of the ROIs were extracted. This point was written to Arduino using PySerial library.

## Arduino code

After declaring variables and attaching servos, we used the points that had been extracted before and wrote them to the servo motor.

