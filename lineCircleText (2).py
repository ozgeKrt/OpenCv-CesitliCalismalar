import cv2
import numpy as np
def main():

    resim=np.zeros((400,400,3),dtype="uint8")

    print(resim)
    print(resim[0][0])      #0. satır 0. sütundaki pikselin değerini alırız.

    cv2.imshow("Arka Plan",resim)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
