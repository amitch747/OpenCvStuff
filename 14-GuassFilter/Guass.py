import cv2 as cv
import os
import numpy as np
import matplotlib.pyplot as plt

def guassianKernel(size,sigma):
    # 1D
    kernel = cv.getGaussianKernel(size,sigma)
    # 2D
    kernel = np.outer(kernel,kernel)
    return kernel

def callback(input):
    pass

def gaussianFiltering():
    root = os.getcwd()
    imgPath = os.path.join(root, 'demoFiles\\cat.jpg')
    img = cv.imread(imgPath)
    
    n = 51
    fig = plt.figure()
    plt.subplot(121)
    kernel = guassianKernel(n,20)
    plt.imshow(kernel)
    
    ax = fig.add_subplot(122,projection='3d')
    x = np.arange(0,n,1)
    y = np.arange(0,n,1)
    X,Y = np.meshgrid(x,y)
    ax.plot_surface(X,Y,kernel, cmap='viridis')


    plt.show()
    
    
    winName = 'gaus filter'
    cv.namedWindow(winName)
    cv.createTrackbar('sigma',winName, 1, 20, callback)
    height,width,_ = img.shape
    scale = 1/4
    width = int(width*scale)
    height = int(height*scale)
    img = cv.resize(img, (width, height))
    
    
    
    while True:
        if cv.waitKey(1) == ord('q'):
            break
    
        sigma = cv.getTrackbarPos('sigma', winName)
        imgFilter = cv.GaussianBlur(img, (n,n), sigma)
        cv.imshow(winName, imgFilter)
        
    cv.destroyAllWindows()
    
    
if __name__ == '__main__':
    gaussianFiltering()