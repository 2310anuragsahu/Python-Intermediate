import cv2


# Colored image
image = cv2.imread("C:/Users/inasahu/Pictures/Doggo.jpg", 1)
print(image.shape)
print(image)

# Displaying the image
cv2.imshow("Doggo Window", image)

cv2.waitKey(0)
# cv2.waitKey(2000)

cv2.destroyAllWindows()
