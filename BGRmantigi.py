import cv2

resim=cv2.imread("TomJerry.jpg")
cv2.imshow("Tom ve Jerry",resim)

print(resim)            #piksellerin matrissel yerlerini bize gösterir.
print(resim.size)       #kaç tane piksel olduğunu verir.    
print(resim.dtype)       #resim hangi data türünden olduğunu gösterir.uint8

print(resim.shape)      #resmin genişliğini yüksekliğini ve kaç tane renk kanalından oluştuğunu bize verir.

print(resim.item(200,100,0))    #166. pikselde(consolda çıktı) bu BGR göre bu rengimiz mevcut
cv2.waitKey(0)
cv2.destroyAllWindow()