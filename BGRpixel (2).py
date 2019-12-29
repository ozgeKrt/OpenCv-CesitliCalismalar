import cv2
import numpy as np

resim=cv2.imread("tazmanya.jpg")
cv2.imshow("Tazmanya Canavarlari",resim)

print(resim[120,50])

print("Resim özelliği..:"+ str(resim.shape))
print("Resim boyutu..:"+ str(resim.size))
print("Resim bit değeri..:"+ str(resim.dtype))       #kaç pikselden oluştuğunu görmek için


cv2.waitKey(0)
cv2.destroyAllWindows()