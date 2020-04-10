import cv2


# Colored image
image = cv2.imread("C:/Users/inasahu/Pictures/Doggo.jpg", 1)
print(image.shape)
print(image)

# Displaying the image
cv2.imshow("Doggo Window", image)
cv2.waitKey(2000)

# Resizing the image asymmetrically
resized_img = cv2.resize(image, (300, 500))
cv2.imshow("Resized Doggo", resized_img)
cv2.waitKey(2000)

# Resizing the image symmetrically
resized_img = cv2.resize(image, (int(image.shape[1]/2), int(image.shape[0]/2)))
cv2.imshow("Resized Doggo New", resized_img)
cv2.waitKey(2000)

cv2.destroyAllWindows()
