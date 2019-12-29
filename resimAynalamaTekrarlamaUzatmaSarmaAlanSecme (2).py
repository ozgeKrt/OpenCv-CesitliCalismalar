import cv2
import numpy as np

resim=cv2.imread("hababamSinifi.jpg")
#print(resim[50,50])     #50 alt 50 sağdaki pikselin BGR değerlerini çıkarır.

cv2.rectangle(resim,(50,200),(150,20),[0,0,255],2)

cv2.imshow("Hababam Sinifi",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()