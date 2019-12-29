import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

dusuk = np.array([90,50,50])
yuksek = np.array([130,255,255])

while True:

    ret,goruntu = kamera.read()

    hsv = cv2.cvtColor(goruntu,cv2.COLOR_BGR2HSV)

    mask=cv2.inRange(hsv,dusuk,yuksek)

    kendiRengi = cv2.bitwise_and(goruntu,goruntu,mask = mask)

    #smoothed
    kernel = np.ones((15,15),dtype = np.float32) / 225 

    smoothed = cv2.filter2D(kendiRengi,-1, kernel)

    #blur
    blur = cv2.GaussianBlur(kendiRengi, (15,15), 0)

    #median
    median=cv2.medianBlur(kendiRengi,15)

    #bilateral
    bilateral = cv2.bilateralFilter(kendiRengi, 15, 75, 75)

    cv2.imshow("ana goruntu",goruntu)
    
    cv2.imshow("hsv",hsv)

    cv2.imshow("mask",mask)

    cv2.imshow("son renk algilama",kendiRengi)
    
    cv2.imshow("smoothed",smoothed)
    
    cv2.imshow("blur",blur)
    
    cv2.imshow("median",median)
    
    cv2.imshow("bilateral",bilateral)
    

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
print(kernel)
kamera.release()
cv2.destroyAllWindows()