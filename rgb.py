import cv2
image = cv2.imread("stranger-things.jpg")
print(image.shape)

for x in range(0, image.shape[0], 1):
    for y in range(0, image.shape[1], 1):
        color = image[y, x]
        print(color)
