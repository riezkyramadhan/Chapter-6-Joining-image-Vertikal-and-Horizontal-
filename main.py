import cv2
import numpy as np 

img = cv2.imread("elon.jpg")
img_resize = cv2.resize(img, (250,250),3)

def horizontal():
    img_hor = np.hstack((img_resize,img_resize,img_resize))
    cv2.imshow("Horizontal", img_hor)
    cv2.waitKey(0)

def vertical():
    img_ver = np.vstack((img_resize,img_resize,img_resize))
    cv2.imshow("Vertical", img_ver)
    cv2.waitKey(0)
    
def comparison():
    img_hor = np.hstack((img_resize,img_resize,img_resize))
    img_ver = np.vstack((img_resize,img_resize,img_resize))
    cv2.imshow("Vertical", img_ver)
    cv2.imshow("Horizontal", img_hor)
    cv2.waitKey(0)

#horizontal()
#vertical()
comparison()