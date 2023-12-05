import cv2

img = cv2.imread('street_car.jpg')

print(type(img))
# The cv2.imread function returns a NumPy array representing the image

print(img.shape)

print(f"Height:{img.shape[0]}")

print(f"Width:{img.shape[1]}")

print(f"Channels:{img.shape[2]}")

cv2.imshow('Image', img)

cv2.waitKey(0)
# cv2.waitKey pauses the execution of the script until we press a key on our keyboard. Using a parameter of 0
# indicates that any keypress will un-pause the execution

# cv2.imwrite("name.jpg", img)
