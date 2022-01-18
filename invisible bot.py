import numpy as np
import cv2
import time
c = cv2.VideoCapture(0)
time.sleep(3)       
bg = 0

for i in range(60):

    ret, bg = c.read()

bg = np.flip(bg,axis=1)
while(c.isOpened()):  

    ret, img = c.read()
    if not ret:
        break
    img = np.flip(img,axis=1)
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([0,120,70])
    upper_red = np.array([10,255,255])

    m1 = cv2.inRange(hsv, lower_red,upper_red)

    lower_red = np.array([170,120,70])
    upper_red =  np.array([180,255,255])
    m2 = cv2.inRange(hsv,lower_red,upper_red)

    m1 = m1 +m2

    m1 = cv2.morphologyEx(m1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8), iterations = 2)
    m1 = cv2.morphologyEx(m1, cv2.MORPH_DILATE,np.ones((3,3),np.uint8), iterations = 1)

    m2 =cv2.bitwise_not(m1)

    r1 = cv2.bitwise_and(bg,bg,mask=m1)
    r2 = cv2.bitwise_and(img,img,mask=m2)
    final_output = cv2.addWeighted(r1,1,r2,1,0)
    cv2.imshow('INVISIBLE BOT',final_output)
    k = cv2.waitKey(10)
    if k==27:
        break
c.release()
Gcv2.destroyAllWindows()
