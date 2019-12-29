import cv2
import numpy as np
def main():

    resim=np.zeros((400,400,3),dtype="uint8")

    cv2.circle(resim,(200,200),50,(0,255,0),2)
    #ikinci parametremiz dairenin merkezi..Üçüncü parametre yarıçap istiyor
    #4. parametre BGR istiyor
    #5.parametrede kalınlık istiyor.

    cv2.imshow("DAIRE",resim)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
