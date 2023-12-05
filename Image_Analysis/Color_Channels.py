import cv2

image = cv2.imread('street_car.jpg')

(B, G, R) = cv2.split(image)

cv2.imshow("Blue", B)
cv2.imshow("Green", G)
cv2.imshow("Red", R)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
(h, s, v) = cv2.split(hsv)

cv2.imshow("Hue", h)
cv2.imshow("Saturation", h)

cv2.imshow("Gray", gray)
cv2.imshow("HSV", hsv)
cv2.waitKey(0)
