import cv2 as cv
import os
import numpy as np
import matplotlib.pyplot as plt

def callback(input):
    pass

def cannyEdge():
    root = os.getcwd()
    imgPath = os.path.join(root, 'demoFiles\\cat.jpg')
    img = cv.imread(imgPath)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    
    height, width, _ = img.shape
    scale = 1/5
    heightScale = int(height*scale)
    widthScale = int(width*scale)
    img = cv.resize(img, (widthScale,heightScale), interpolation=cv.INTER_LINEAR)

    winName = 'canny'
    cv.namedWindow(winName)
    cv.createTrackbar('minThresh', winName, 0, 255, callback)
    cv.createTrackbar('maxThresh', winName, 0, 255, callback)

    while True:
        if cv.waitKey(1) == ord('q'):
            break
        
        minThresh = cv.getTrackbarPos('minThresh', winName)
        maxThresh = cv.getTrackbarPos('maxThresh', winName)
        cannyEdge = cv.Canny(img, minThresh, maxThresh)
        cv.imshow(winName, cannyEdge)
    
    cv.destroyAllWindows()


if __name__ == '__main__':
    cannyEdge()
    