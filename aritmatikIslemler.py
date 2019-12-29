import cv2
import numpy as np

    cem_Yilmaz=cv2.imread("cemYilmaz.jpg")
    android=cv2.imread("android.png")

    a_gri=cv2.cvtColor(android,cv2.COLOR_BGR2GRAY)      #resmi griye çevirdik. imread fonksiyonun 2. parametresine 0 deseydik de griye çevirebilirdik.
    yukseklik,genislik,kanal=android.shape      #shape de zaten 3 tane değişken var üçünü de otomatik sırayla değişkenlere verir

    print(yukseklik,genislik,kanal)



    cv2.imshow("Cem Yilmaz",cem_Yilmaz)
    cv2.imshow("Android", a_gri)


    cv2.waitKey(0)
    cv2.destroyAllWindows()