import cv2
import numpy as np
def main():

    resim=np.zeros((400,400,3),dtype="uint8")

    cv2.putText(resim,"Ozge Kurt",(150,150),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),3)
    #ikinci parametremiz yazmak istediğim yazı..Üçüncü parametre bu yazımızın başlangıç pikselini istiyor.
    #4. parametre yazı tipi özelliği istiyor.
    #5.parametrede yazının boyutunu istiyor.
    #6. parametrede BGR istiyor.
    #7.parametre yazımın çizgi boyutu

    cv2.imshow("TEXT",resim)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
