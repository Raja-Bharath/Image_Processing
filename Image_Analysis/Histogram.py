import cv2
from matplotlib import pyplot as plt

image = cv2.imread('street_car.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

plt.figure()
plt.title("Histogram of Image")
plt.xlabel("Bins")
plt.ylabel("No: of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()

# chans = cv2.split(image)
# colors = ("b", "g", "r")
# plt.figure()
# plt.title("Color Histogram")
# plt.xlabel("Bins")
# plt.ylabel("No: of Pixels")
#
# for (chan, color) in zip(chans, colors):
#     hist_color = cv2.calcHist([chan], [0], None, [256], [0, 256])
#     plt.plot(hist_color, color=color)
#     plt.xlim([0, 256])
#     plt.show()
#
# cv2.waitKey(0)
