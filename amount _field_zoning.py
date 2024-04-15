import numpy as np
import cv2
import math
image = cv2.imread('0.jpg')
y, x = image.shape[:2]
print(image.shape)
print(x,y)
x_w, y_h = math.floor(x//2) , math.floor(y//2)
print(x_w, y_h)
# print(math.floor(x/2))
# print(math.floor(y/2))
# print(x, y, x_w, y_h)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray_image, 100, 200)
lines = cv2. HoughLinesP(edges, 1, np.pi/180, 100, 200)
#for line in lines:
  #x1, y1, x2, y2 = line[0]
  #cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
  #print(line)
cv2.line(image, (x_w, 0), (x_w, y), (0, 255, 0), 2)
#cv2.line(image, (2*x_w, 0), (2*x_w, y), (0, 255, 0), 2)
#cv2.line(image, (3*x_w, 0), (3*x_w, y), (0, 255, 0), 2)

cv2.line(image, (0, y_h), (x, y_h), (0, 255, 0), 2)
#cv2.line(image, (0, 2*y_h), (x, 2*y_h), (0, 255, 0), 2)
#cv2.line(image, (0, 3*y_h), (x, 3*y_h), (0, 255, 0), 2)

cv2.imshow('Detected Lines', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
