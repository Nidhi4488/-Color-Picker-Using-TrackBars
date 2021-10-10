#Building Color picker using Trackbars
import cv2
import numpy as np

def cross(x):
    pass

#blank
img=np.zeros((300,500,3),np.uint8)
cv2.namedWindow("Color Picker")

#Create Switch
s1="0:OFF \n 1:ON"
                  #string message to be passed, window name, value,if nthing then call this function
cv2.createTrackbar(s1,"Color Picker",0,1,cross)

#creating for rgb
#creating trackbars for adjusting colors
cv2.createTrackbar("R","Color Picker",0,255,cross)
cv2.createTrackbar("G","Color Picker",0,255,cross)
cv2.createTrackbar("B","Color Picker",0,255,cross)

while True:
    cv2.imshow("Color Picker",img)
    if cv2.waitKey(1)==27:
        break

    #getting trackbar position
    s=cv2.getTrackbarPos(s1,"Color Picker")
    r=cv2.getTrackbarPos("R","Color Picker")
    g=cv2.getTrackbarPos("G","Color Picker")
    b=cv2.getTrackbarPos("B","Color Picker")

    if s==0:
        img[:]=0 #all the pixels of image
    else:
        img[:]=[r,g,b]
cv2.destroyAllWindows()


