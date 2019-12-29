import cv2
import numpy as np

resim=cv2.imread("senerSen.jpg")

#resim[:,:,0]=255        #0. kanal blue'dur. Resmin herbir pikselinin BGR'sinde mavi pikselleri  fullenir.
#resim[:,:,1]=255       #1.kanal green'dir. 
#resim[:,:,2]=255       #2. kanal red'dir.

resim[100:200,200:400,0]=255        #y de 100 ile 200 pikselin arası;
# x de 200 ile piksel arası mavi kanalın (0) değerini 255 yapmak istersem.

cv2.imshow("Sener Sen",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()