import cv2 as cv
import os
import numpy as np
import matplotlib.pyplot as plt


def HSV():
    root = os.getcwd()
    imgPath = os.path.join(root, 'demoFiles\\whoa.png')
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    # b,g,r = cv.split(img)

    # cmax = max(b,g,r)
    # cmin = min(b,g,r)
    # diff = cmax-cmin
    
    # #HUE
    # if (cmax == cmin):
    #     hue = 0
    # elif (cmax == r):
    #     hue = (60*((g-b)/diff)+360) % 360
    # elif (cmax == g):
    #     hue = (60*((b-r)/diff)+120) % 360
    # elif (cmax == b):
    #     hue = (60*((r-g)/diff)+240) % 360
    hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    lowerBound = np.array([0, 0, 0])     
    upperBound = np.array([40, 80, 255])
    # h25 s20 b95
    mask = cv.inRange(hsv, lowerBound, upperBound)
    
    plt.figure()
    plt.imshow(hsv)
    plt.show()
    
    plt.figure()
    plt.imshow(mask)
    plt.show()
    # cv.imShow('mask', mask)
    # cv.waitKey(0)
    
    
if __name__ == '__main__':
    HSV()
    