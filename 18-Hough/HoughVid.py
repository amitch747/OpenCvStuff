import cv2 as cv
import os
import numpy as np
import matplotlib.pyplot as plt



def houghLineTransform(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    imgBlur = cv.GaussianBlur(gray, (21, 21), 3)
    cannyEdge = cv.Canny(imgBlur, 30, 60)
    
    distResol = 1
    angleResol = np.pi / 180
    threshold = 80
    lines = cv.HoughLines(cannyEdge, distResol, angleResol, threshold)
    k = 3000

    imgOut = img.copy()

    if lines is not None:
        for curLine in lines:
            rho, theta = curLine[0]
            dhat = np.array([[np.cos(theta)], [np.sin(theta)]])
            d = rho * dhat
            lhat = np.array([[-np.sin(theta)], [np.cos(theta)]])
            p1 = d + k * lhat
            p2 = d - k * lhat

            p1 = p1.astype(int)
            p2 = p2.astype(int)
            cv.line(imgOut, (p1[0][0], p1[1][0]), (p2[0][0], p2[1][0]), (255, 255, 255), 2)

    return imgOut


def videoFromWebcam():
    cap = cv.VideoCapture(0)
    sift = cv.SIFT_create()

    if not cap.isOpened():
        exit()
        
    while True:
        ret, frame = cap.read()
        if ret:
            frame = houghLineTransform(frame)

            cv.imshow('Webcam', frame)
            
        if cv.waitKey(1) == ord('q'):
            break
    
    cap.release()
    cv.destroyAllWindows()

 


if __name__ == '__main__':
    videoFromWebcam()