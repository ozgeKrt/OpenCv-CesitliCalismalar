import cv2
import numpy as np
def main():

    resim=np.zeros((400,400,3),dtype="uint8")      #400e400 bir matris oluştursun her matrisi de 3 tane yapı tutuyor.
    print(resim)



cv2.waitKey(0)
cv2.destroyAllWindows()

if __name__ == '__main__':
    main()