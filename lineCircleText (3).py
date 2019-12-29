import cv2
import numpy as np
def main():

    resim=np.zeros((400,400,3),dtype="uint8")

    cv2.line(resim,(0,0),(200,200),(255,0,0),2)
    #ikinci parametremiz çizgi nereden başlasın.üçüncü parametre nereye lkadar gideceği
    #4.parametre BGR 5.parametre çizginin kalınlığı

    cv2.imshow("CIZGI CEKME",resim)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
