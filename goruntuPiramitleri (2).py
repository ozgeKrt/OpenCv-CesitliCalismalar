import cv2
import numpy as np

def main():

    resim=cv2.imread("resim.jpg")
    
    
    print(resim.shape)           #resmin yukseklik genislik ve kanallarını bulur
    iki_kat=cv2.pyrUp(resim)              #resim kenarlar olarak iki kat artar  
    iki_kat_kucuk=cv2.pyrDown(resim)      #resim kenarlar olarak iki kat küçülür.

    print("İki kat büyük",iki_kat.shape)
    print("İki kat küçük",iki_kat_kucuk.shape)

    cv2.imshow("Resim",resim)
    cv2.imshow("İki katına çıkmış resim",iki_kat)
    cv2.imshow("İki katı küçülmüş resim",iki_kat_kucuk)

    cv2.waitKey(0)
    cv2.destroyAllWindows()



if __name__ == '__main__':
    main()