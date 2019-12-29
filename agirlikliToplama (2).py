import cv2
import numpy as np

def main():
    resim1=cv2.imread("emelSayin.jpg")
    resim2=cv2.imread("tarikAkan.jpg")

    print(resim1[200,200])
    print(resim2[200,200])

    print(resim1[200,200]+resim2[200,200])

   # toplam=cv2.add(resim1,resim2)

    cv2.imshow("Emel Sayin",resim1)
    cv2.imshow("Tarık Akan",resim2)
    #cv2.imshow("Toplam",toplam)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()