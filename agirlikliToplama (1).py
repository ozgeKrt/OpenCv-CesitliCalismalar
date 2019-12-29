import cv2
import numpy as np

def main():
    resim1=cv2.imread("emelSayin.jpg")
    resim2=cv2.imread("tarikAkan.jpg")

    print(resim1[200,200])
    print("/n")
    print(resim2[200,200])

    cv2.imshow("Emel Sayin",resim1)
    cv2.imshow("Tarık Akan",resim2)
    
    toplam = cv2.add(resim1,resim2)

    print(toplam[200,200])
    print("/n")

    agirlikli_toplam=cv2.addWeighted(resim1,0.2,resim2,0.8,0)  

    print(agirlikli_toplam[200,200])

    cv2.imshow("toplam",toplam)
    cv2.imshow("Agirlikli Toplam",agirlikli_toplam) 

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()