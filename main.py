import numpy as np
import cv2


#capture the webcam
vid1 = cv2.VideoCapture(0)
vid2 = cv2.VideoCapture(1)
vid3 = cv2.VideoCapture('http://192.168.2.2:5000/video')  #ipwebcam address 


while True:                               #while true, read the camera
    ret , frame = vid1.read()
    re1 , frame1 = vid2.read()
    ret2 , frame2 = vid3.read()

    if (ret):
        cv2.imshow('cam0',frame)            #frame with name and variable of the camera 
        cv2.imshow('cam1', frame1)
        cv2.imshow('cam3',frame2)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):      #to break the loop and terminate the program 
        break

vid1.release()
vid2.release()
vid3.release()






