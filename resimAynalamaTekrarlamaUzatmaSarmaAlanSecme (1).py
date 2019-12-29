import cv2
import numpy as np

resim=cv2.imread("adileNasit.jpg")

#resmi uzatma
uzatilan_resim=cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_REPLICATE)

#resmi aynalama
aynalanan_resim=cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_REFLECT)

#resmi tekrar etme
tekrarlanan_resim=cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_WRAP)

#resmin etrafını sarma
sarilan_resim=cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_CONSTANT,value=(255,0,0))

cv2.imshow("Adile Nasit Orijinal",resim)
cv2.imshow("Adile Nasit Uzatma",uzatilan_resim)
cv2.imshow("Adile Nasit Aynalama",aynalanan_resim)
cv2.imshow("Adile Nasit Tekrar Etme",tekrarlanan_resim)
cv2.imshow("Adile Nasit Sarma",sarilan_resim)

cv2.waitKey(0)
cv2.destroyAllWindows()