import cv2
image = cv2.imread("stranger-things.jpg")
edge = cv2.Canny(image, 10, 20)
cv2.imshow("Edge Detect", edge)
cv2.waitKey(0)