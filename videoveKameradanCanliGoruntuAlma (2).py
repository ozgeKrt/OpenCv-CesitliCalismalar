import cv2
import numpy as np

kamera=cv2.VideoCapture(0)

while True:
    ret,kare=kamera.read()      #kameranın çalışıp çalışmadığını kontrol eder.

    bolge=kare[0:200,0:200]

    cv2.imshow("Video",kare)        
    cv2.imshow("Bolge",bolge)

    if cv2.waitKey(25) & 0xFF ==('q'):
        break

kamera.release()
    

cv2.destroyAllWindows()
