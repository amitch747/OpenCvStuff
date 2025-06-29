import cv2 as cv
import os
import numpy as np
import matplotlib.pyplot as plt

def grayHistogram():
    root = os.getcwd()
    imgPath = os.path.join(root, 'demoFiles\\cat.jpg')
    img = cv.imread(imgPath, cv.IMREAD_GRAYSCALE)
    
    plt.figure()
    plt.imshow(img, cmap='gray')
    
    hist = cv.calcHist([img], [0], None, [256], [0,256])
    plt.figure()
    plt.plot(hist)
    plt.xlabel('bins')
    plt.ylabel('# of pixels')
    plt.show()
    
def colorHistogram():
    root = os.getcwd()
    imgPath = os.path.join(root, 'demoFiles\\cat.jpg')
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    
    plt.figure()
    plt.imshow(imgRGB)
    
    colors = ['b','g','r']
    plt.figure()
    for i in range(len(colors)):
        hist = cv.calcHist([imgRGB],[i],None,[256],[0,256])
        plt.plot(hist,colors[i])
        
    plt.xlabel('pixel intensity')
    plt.ylabel('# of pixels')
    
    
    plt.show()
    
    
if __name__ == '__main__':
    colorHistogram()
