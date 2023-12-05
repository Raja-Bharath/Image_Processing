import cv2
import numpy as np

image = np.zeros((300, 300, 3), dtype='uint8')

image_copy = np.zeros((300, 300, 3), dtype='uint8')

cv2.line(image, (0, 0), (300, 300), (0, 255, 255), 2)

cv2.rectangle(image, (50, 200), (200, 225), (0, 0, 255), -1)

(centerX, centerY) = (image.shape[1] // 2, image.shape[0] // 2)

for r in range(0, 175, 25):
    cv2.circle(image, (centerX, centerY), r, (255, 255, 255))

for i in range(0, 25):
    radius = np.random.randint(5, high=200)
    color = np.random.randint(0, high=256, size=(3,)).tolist()
    pt = np.random.randint(0, high=300, size=(2,))

    cv2.circle(image_copy, tuple(pt), radius, color, -1)

cv2.imshow("Image Window", image_copy)
cv2.waitKey(0)

cv2.imshow("Image Window", image)

cv2.waitKey(0)

"""
Points to be noted:

Since we are representing our image as an RGB image with pixels
in the range [0, 255], it’s important that we use an 8-bit unsigned integer.

We just pass in a negative value for the thickness
argument to obtain filled shape.

(3,) indicates that the array has one dimension.

For example, if you create a NumPy array with a = np.array([1, 2, 3]), 
the shape of a would be (3,) because it has one dimension of size 3.
"""
