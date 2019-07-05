import cv2
import numpy as np
import matplotlib.pyplot as plt
# show OpenCV version
print(cv2.__version__)
#read the iamge and convert to grayscale
image = cv2.imread('stranger-things.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#create sift object
sift = cv2.xfeatures2d.SIFT_create()
#calculate keypoints and their orientation
keypoints, descriptors = sift.detectAndCompute(gray, None)
#plot keypoints on the image
with_keypoints = cv2.drawKeypoints(gray, keypoints)
# plot the image
plt.imshow(with_keypoints)