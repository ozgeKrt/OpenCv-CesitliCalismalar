import cv2
import numpy as np

kamera=cv2.VideoCapture(0)      #kendi bilgisayarıma bağımlı kullandığım için

def main():
    while True:
        ret,kare=kamera.read()      #ret parametresinin döndürdüğü değer kameram çalıştığı için true olacak
                                    #kare adlı değişkenimin döndürdüğü değer de np sınıfından bir obje
                                    #bu obje de bizim piksellerimizi bütün kameranın fotoğrafındaki piksellere dönüştürür

        cv2.imshow("Kare",kare)     #aldığım kareleri gösteririm.


if cv2.waitKey(25) & 0xFF == ord('q'):      #kareler her 25 ms de bir yenilensin. q ya basıldığında çıkış olur.
    break

kamera.release()        #döngüden çıktıktan sonra kamera görüntü almayı bırakır.

cv2.destroyAllWindows()

if __name__ == "__main__":
    main()