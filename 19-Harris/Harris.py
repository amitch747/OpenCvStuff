import cv2 as cv
import os
import numpy as np
import matplotlib.pyplot as plt

def harrisCorner(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    
    blockSize = 5
    sobelSize = 3
    k = 0.04
    harris = cv.cornerHarris(gray, blockSize, sobelSize, k)

    img[harris>0.05*harris.max()] = [255,0,0]
    return img

def videoFromWebcam():
    cap = cv.VideoCapture(0)
    sift = cv.SIFT_create()

    if not cap.isOpened():
        exit()
        
    while True:
        ret, frame = cap.read()
        if ret:
            frame = harrisCorner(frame)

            cv.imshow('Webcam', frame)
            
        if cv.waitKey(1) == ord('q'):
            break
    
    cap.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    videoFromWebcam()