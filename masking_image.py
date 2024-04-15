import cv2
path = 'C:\\Users\Patterns\Desktop\Assassins.jpg'
image = cv2.imread(path)
height, width = image.shape[:2]
print(image.shape)
starting_coordinates = (0,0)
ending_coordinates = (100,100)
left_corner = [starting_coordinates,ending_coordinates]
color = (0, 0, 255)
image = cv2.rectangle(image, starting_coordinates, ending_coordinates, color, -1)
window_name = 'image'
cv2.imshow(window_name,image)
cv2.waitKey(0)