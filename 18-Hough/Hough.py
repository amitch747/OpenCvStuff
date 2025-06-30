import cv2 as cv
import os
import numpy as np
import matplotlib.pyplot as plt


def houghLineTransform():
    root = os.getcwd()
    imgPath = os.path.join(root, 'demoFiles\\cat.jpg')
    img = cv.imread(imgPath, cv.IMREAD_GRAYSCALE)
    imgBlur = cv.GaussianBlur(img, (21,21),3)
    cannyEdge = cv.Canny(imgBlur, 30,60)
    
    plt.figure(figsize=(16, 4))

    plt.subplot(131)
    plt.imshow(imgBlur)
    plt.subplot(132)
    plt.imshow(cannyEdge)

    distResol = 1
    angleResol = np.pi/180
    threshold = 180
    lines = cv.HoughLines(cannyEdge, distResol, angleResol, threshold)
    
    k = 3000
    
    # Need to look into why this works more
    for curLine in lines:
        rho,theta = curLine[0]
        dhat = np.array([[np.cos(theta)], [np.sin(theta)]])
        d = rho*dhat
        lhat = np.array([[-np.sin(theta)], [np.cos(theta)]])
        p1 = d + k*lhat
        p2 = d - k*lhat
        
        p1 = p1.astype(int)
        p2 = p2.astype(int)
        cv.line(img, (p1[0][0], p1[1][0]), (p2[0][0],p2[1][0]), (255,255,255), 10)
        
    
    plt.subplot(133)
    plt.imshow(img)
    plt.show()

if __name__ == '__main__':
    houghLineTransform()