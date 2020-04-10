import cv2


# Colored image
image = cv2.imread("C:/Users/inasahu/Pictures/Doggo.jpg", 1)
print(image.shape)
print(image)

# Black and White image
image2 = cv2.imread("C:/Users/inasahu/Pictures/Doggo.jpg", 0)
print('\n', image2.shape)
print(image2)

