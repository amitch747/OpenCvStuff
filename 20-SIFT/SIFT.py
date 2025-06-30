import cv2 as cv
import os
import numpy as np
import matplotlib.pyplot as plt

def SIFT():
    root = os.getcwd()
    imgPath = os.path.join(root, 'demoFiles\\cat.jpg')
    imgGray = cv.imread(imgPath, cv.IMREAD_GRAYSCALE)
    
    sift = cv.SIFT_create()
    keypoints = sift.detect(imgGray, None)
    imgGray = cv.drawKeypoints(imgGray, keypoints, imgGray, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    
    plt.figure()
    plt.imshow(imgGray)
    plt.show()
    
if __name__ == '__main__':
    SIFT()