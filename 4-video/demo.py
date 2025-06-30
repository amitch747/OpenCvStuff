import numpy as np
import cv2 as cv
import os
import matplotlib.pyplot as plt


def videoFromWebcam():
    cap = cv.VideoCapture(0)
    sift = cv.SIFT_create()

    if not cap.isOpened():
        exit()
        
    while True:
        ret, frame = cap.read()
        if ret:
            keypoints = sift.detect(frame, None)
            frame = cv.drawKeypoints(frame, keypoints, frame, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

            cv.imshow('Webcam', frame)
            
        if cv.waitKey(1) == ord('q'):
            break
    
    cap.release()
    cv.destroyAllWindows()
    
def videoFromFile():
    root = os.getcwd()
    vidPath = os.path.join(root, 'demoFiles\leg.mp4')
    cap = cv.VideoCapture(vidPath)
    
    while cap.isOpened():
        ret, frame = cap.read()
        cv.imshow('video', frame)
        delay = int(1000/60)
        if cv.waitKey(delay) == ord('q'):
            break
    
if __name__ == '__main__':
    videoFromWebcam()
