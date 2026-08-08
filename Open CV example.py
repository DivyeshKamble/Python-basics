import cv2
import os
import sys

IMAGE_PATH = r"Put the path of your image here" #here put the path of your image for viewing it using OpenCV

if not os.path.isfile(IMAGE_PATH):
	print(f"Error: image file not found: {os.path.abspath(IMAGE_PATH)}")
	sys.exit(1)

img = cv2.imread(IMAGE_PATH)
if img is None:
	print(f"Error: failed to load image: {os.path.abspath(IMAGE_PATH)}")
	sys.exit(1)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()