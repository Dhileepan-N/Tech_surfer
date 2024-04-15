import cv2
import os

import numpy as np

date_specimen = cv2.imread('date_specimen.JPG')
cheque_image = cv2.imread('C-7758832BW.jpg')
h,w,d = date_specimen.shape
h1,w1,d1 = cheque_image.shape
print(str(h) +','+ str(w)+ ',' +str(d))
print(str(h1) +','+ str(w1)+ ',' +str(d1))
#diff = cv2.subtract(cheque_image,cheque_image)
#err = np.sum(diff**2)
#print(err)
for i in range(h1):
    for j in range(w1):
        crop = cheque_image[i:i+26, j:j+46]
        print(str(crop.shape))
        #cv2.imshow('crop',crop)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        #diff = cv2.subtract(crop, date_specimen)
        #err = np.sum(diff ** 2)
        #if err == 0:
            #print(str(i)+','+str(j))