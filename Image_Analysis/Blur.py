import cv2
import numpy as np

image = cv2.imread('street_car.jpg')

blur_image = np.hstack([cv2.blur(image, (3, 3)),
                        cv2.blur(image, (5, 5)),
                        cv2.blur(image, (7, 7))])

gaussian_blur_image = np.hstack([cv2.GaussianBlur(image, (3, 3), 0),
                                 cv2.GaussianBlur(image, (5, 5), 0),
                                 cv2.GaussianBlur(image, (7, 7), 0)])

cv2.imshow("Blur Image", blur_image)
cv2.imshow("Gaussian Blur Image", gaussian_blur_image)
cv2.waitKey(0)


"""
Points to be noted:
A smaller standard deviation results in a narrower Gaussian distribution, 
meaning that neighboring pixels close to the center pixel will be weighted more heavily.
"""