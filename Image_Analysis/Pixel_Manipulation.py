import cv2

image = cv2.imread('street_car.jpg')

(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

corner = image[0:50, 0:100]
cv2.imshow("Corner", corner)

image[0:50, 0:100] = (0, 255, 0)

cv2.imshow("Updated", image)
cv2.waitKey(0)

