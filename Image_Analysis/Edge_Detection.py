import cv2

image = cv2.imread('street_car.jpg')

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image = cv2.GaussianBlur(image, (5, 5), 0)

canny = cv2.Canny(image, 30, 150)

cv2.imshow("Canny", canny)
cv2.waitKey(0)
