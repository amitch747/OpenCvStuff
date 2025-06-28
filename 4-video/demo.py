import numpy as np
import cv2 as cv
import os


def videoFromWebcam():
    cap = cv.VideoCapture(0)
    
    if not cap.isOpened():
        exit()
        
    while True:
        ret, frame = cap.read()
        if ret:
            cv.imshow('Webcam', frame)
            
        if cv.waitKey(1) == ord('q'):
            break
    
    cap.release()
    cv.destroyAllWindows()
    
if __name__ == '__main__':
    videoFromWebcam()