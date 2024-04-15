import cv2
import numpy as np
from PIL import Image
import math
count = 0
count1 = 0
image = cv2.imread('C-7758832BW.jpg')
image2 = image.copy()
edged = cv2.Canny(image,30,300)
edged2 = cv2.Canny(image2,30,300)
lines = cv2.HoughLinesP(edged,rho =1,theta=1*np.pi/180,threshold=127,minLineLength=536,maxLineGap=14)
v_lines = cv2.HoughLinesP(edged,rho =1,theta=1*np.pi/180,threshold=127,minLineLength=15,maxLineGap=4)
sign_lines = cv2.HoughLinesP(edged2,rho =1,theta=1*np.pi/180,threshold=127,minLineLength=14,maxLineGap=4)
for i in reversed(lines):
    #print(len(lines))
    print(i)
    x1,y1,x2,y2 = i[0]
    angle = math.atan2(y2-y1,x2-x1,) * 180.0/ np.pi
    if angle == 0.0 or angle == 180.0:
        cv2.rectangle(image,(x1,y1),(x2,y2),(0,0,255),2)
    count += 1
    if count == 2:
        break
for j in reversed(sign_lines):
    #print(len(lines))
    #print(j)
    x1,y1,x2,y2 = j[0]
    angle = math.atan2(y2-y1,x2-x1,) * 180.0/ np.pi
    if angle == 0.0 or angle == 180.0:
        cv2.rectangle(image2,(x1,y1),(x2,y2),(0,0,255),2)
    count1 += 1
    if count1 == 50:
        break
# for j in reversed(v_lines):
#     #print(len(lines))
#     print(j)
#     x1,y1,x2,y2 = j[0]
#     angle = math.atan2(y2-y1,x2-x1,) * 180.0/ np.pi
#     if angle == 90.0 or angle == 270.0:
#         cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imshow('Contours', image)
#cv2.imshow('sign', image2)

cv2.waitKey(0)
cv2.destroyAllWindows()