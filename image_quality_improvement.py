import cv2
cheque_image = cv2.imread('0.jpg')
threshold = 120
gray_img = cv2.cvtColor(cheque_image, cv2.COLOR_BGR2GRAY)
cheque_image_bw = cv2.threshold(gray_img,threshold,255,cv2.THRESH_BINARY)[1]
#cheque_image_bw = cv2.threshold(cheque_image,threshold,255,cv2.THRESH_TOZERO)[1]
cv2.imwrite('C-7758832BW.jpg', cheque_image_bw)
cv2.imshow('cheque image', cheque_image_bw)
cv2.waitKey(0)