import cv2
import numpy as np

#0 ==> bilgisayardaki tanımlı olan kamerayı kullanıcak
#1 ==>usb
#2 ==>video

kamera=cv2.VideoCapture(0)

while True:
    ret,kare=kamera.read()      #kameranın çalışıp çalışmadığını kontrol eder.

    cv2.rectangle(kare,(100,200),(200,100),(255,0,0),2)     #kamerada bir kare oluşturduk belirttiğimiz konumlarda

    cv2.imshow("Video",kare)        #her 25 ms de bir kare gönderir ve video oluşur.

    if cv2.waitKey(25) & 0xFF ==('q'):
        break

kamera.release()
    

cv2.destroyAllWindows()
