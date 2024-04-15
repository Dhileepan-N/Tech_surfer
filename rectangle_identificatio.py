import cv2
import numpy as np
from skimage.util import invert

img = cv2.imread('0.jpg')
img_cropped = img[345:690,400:1229].copy()
hieght, width = img.shape[:2]
hieght_half , width_half = hieght//2 , width//2
kernel = np.array([[-1,-1,-1],[-1,8300000,-1],[-1,-1,-1]])
image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )
quality = cv2.threshold(image,115,255,cv2.THRESH_BINARY)[1]
kernel_sharp = cv2.filter2D(quality,-1,kernel)
kernel_sharp_cropped = kernel_sharp[345:690,100:1229].copy()
cv2.imshow('Q', kernel_sharp_cropped)
inv = invert(kernel_sharp_cropped)
#print(inv.dtype)
contours, hierarchy = cv2.findContours(inv,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))
for i,cnt in enumerate(contours):
    approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
    x, y, w, h = cv2.boundingRect(approx)
    img = cv2.rectangle(img_cropped, (x, y), (x + w, y + h), (0, 255, 0), 1)
    # if len(approx) == 4:
    #      x, y, w, h = cv2.boundingRect(approx)
    #      ratio = float(w) / h
    #      if not (ratio >= 0.9 and ratio <= 1.1) and i==204:
    #          print(i)
    #          img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # cv2.drawContours(img, cnt, -1, (0, 255, 0), 3)
#img = cv2.rectangle(img, (921, 333), (1195, 400), (0, 255, 0), 2)
cv2.imshow('shapes', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
