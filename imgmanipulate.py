import cv2

image = cv2.imread("stranger-things.jpg")
cv2.imshow("original", image)
cv2.waitKey(0)
# Getting the shape Height,Width,Colour Scheme
print(image.shape)
print(image.shape[0])
print(image.shape[1])
# Cropping an Image
cropped = image[100:700, 0:400]
cv2.imshow("cropped", cropped)
cv2.waitKey(0)
cv2.imwrite("cropped.jpg", cropped)
# Resizing an Image programmaticaly
r = 1000.0 / image.shape[1]
dim = (1000, int(image.shape[0] * r))
resized_inter_area = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized Inter Area", resized_inter_area)
cv2.waitKey(0)
resized_inter_nearest = cv2.resize(image, dim, interpolation=cv2.INTER_NEAREST)
cv2.imshow("Resized Nearest ", resized_inter_nearest)
cv2.waitKey(0)
resized_inter_cubic = cv2.resize(image, dim, interpolation=cv2.INTER_CUBIC)
cv2.imshow("Resized Cubic", resized_inter_cubic)
cv2.waitKey(0)
resized_inter_linear = cv2.resize(image, dim, interpolation=cv2.INTER_LINEAR)
cv2.imshow("Resized Linear", resized_inter_linear)
cv2.waitKey(0)
resized_inter_lanczos4 = cv2.resize(image, dim, interpolation=cv2.INTER_LANCZOS4)
cv2.imshow("Resized Lanczos4", resized_inter_lanczos4)
cv2.waitKey(0)
# Resize using resize function
new_resize = cv2.resize(image, (1000, 700))
cv2.imshow("New Resize", new_resize)
print(new_resize.shape)
cv2.waitKey(0)


