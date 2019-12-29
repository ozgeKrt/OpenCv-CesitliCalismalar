import cv2
import numpy as np

resim=cv2.imread("nesetErtas.jpg")

bolge=resim[100:300,200:400]
resim[0:200,0:200]=bolge        # üstte tanımlanan ve kesilen bölgeyi şimdi belirlenen resminde belirlediğimiz alana yapıştır.

cv2.imshow("Saz",resim)
cv2.imshow("Resmin kesilen bolgesi",bolge)

cv2.waitKey(0)
cv2.destroyAllWindows()