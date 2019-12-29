import cv2
import numpy as np


resim=cv2.imread("sirinler.jpg")      

resim[20,50]=[255,255,255]      #20 ve 50 koordinatlarındaki pikselin piksel BGR 'sini 255,255,255 yani beyaz yaptık.

for i in range (200):
    resim[150,i]=[255,255,255]

cv2.imshow("Sirinler Kasabasi",resim)   #ilk parametrede windowsa isim veririz ikinci parametrede gösterilecek resmi belirtiriz.


cv2.waitKey(0)
cv2.destroyAllWindows()