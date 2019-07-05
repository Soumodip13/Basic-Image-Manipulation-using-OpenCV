import cv2
import numpy
import matplotlib.pyplot as plt
image = cv2.imread('stranger-things.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# plotting the image
plt.imshow(image)

# saving image
cv2.imwrite('test_write.jpg', image)
