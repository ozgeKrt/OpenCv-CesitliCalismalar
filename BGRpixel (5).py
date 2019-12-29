import cv2
import numpy as np

resim=cv2.imread("kemalSunal.jpg")
b,g,r=cv2.split(resim)      #b,g,r 'a yırdık liste elemanları gibi. Kırmızı çıkan daha beyaz olur insan yüzünde kan olduğundan dolayı

cv2.imshow("Kemal Sunal Orijinal",resim)
cv2.imshow("Kemal Sunal blue",b)
cv2.imshow("Kemal Sunal green",g)
cv2.imshow("Kemal Sunal red",r)

cv2.waitKey(0)
cv2.destroyAllWindows()