import cv2
import numpy as np

image = cv2.imread('street_car.jpg')

translation_matrix = np.float32([[1, 0, 25], [0, 1, 50]])

shifted_image = cv2.warpAffine(image, translation_matrix, (image.shape[1], image.shape[0]))

(h, w) = image.shape[:2]
center = (w // 2, h // 2)

M = cv2.getRotationMatrix2D(center, 45, 1)

rotated = cv2.warpAffine(image, M, (w, h))

resized_image = cv2.resize(image, center, interpolation=cv2.INTER_AREA)


cv2.imshow("Shifted Image", shifted_image)
cv2.imshow("Rotated by 45 Degrees", rotated)
cv2.imshow("Resized Image", resized_image)


cv2.waitKey(0)

"""
Points to be noted:

Our translation matrix M is defined as a floating point
array – this is important because OpenCV expects this matrix to be of floating point type. 
The first row of the matrix is [1, 0, tx], where tx is the number of pixels we will shift
the image left or right. Negative values of tx will shift the image to the left and 
positive values will shift the image to the right.
Then, we define the second row of the matrix as [0, 1, ty],
where ty is the number of pixels we will shift the image up
or down. Negative value of ty will shift the image up and
positive values will shift the image down
"""
