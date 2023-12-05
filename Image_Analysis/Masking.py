import cv2
import numpy as np

image = cv2.imread('street_car.jpg')

img_np = np.zeros((image.shape[:2]), dtype="uint8")

(h, w) = img_np.shape[:2]

mask = cv2.rectangle(img_np, (w - 175, h - 175), (w + 175, h + 175), (255, 255, 255), -1)

image_mask = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Mask", mask)

cv2.imshow("Masked Image",image_mask)

cv2.waitKey(0)
