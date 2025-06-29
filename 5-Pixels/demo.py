import cv2 as cv
import os
import matplotlib.pyplot as plt

def readAndWriteSinglePixel():
    root = os.getcwd()
    imgPath = os.path.join(root, 'demoFiles\\cat.jpg')
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    

    
    eye = imgRGB[343, 703]
    imgRGB[343, 703] = (255,0,0)
    
    plt.figure()
    plt.imshow(imgRGB)
    plt.show()
    
    
def readAndWritePixelRegion():
    root = os.getcwd()
    imgPath = os.path.join(root, 'demoFiles\\cat.jpg')
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    
    # plt.figure()
    # plt.imshow(imgRGB)
    # plt.show()
    
    eyeRegion = imgRGB[336:346,698:709]
    
    width = 709 - 698  
    height = 346 - 336  
    
    startX = 720
    startY = 313
    
    imgRGB[startY:startY+height, startX:startX+width] = eyeRegion
    plt.figure()
    plt.imshow(imgRGB)
    plt.show()

if __name__ == '__main__':
    readAndWritePixelRegion()
    
