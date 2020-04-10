import cv2


# Create a CascadeClassifier Object
face_cascade = cv2.CascadeClassifier("C:/Users/inasahu/PycharmProjects/Python-Intermediate/OpenCV"
                                     "/haarcascade_frontalface_default.xml")

# Reading my Vanderlande image
img = cv2.imread("C:/Users/inasahu/Pictures/Capture.jpg")

# Reading the image as Gray Scale image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# Search the co-ordinates of the image
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)

# Adding the Rectangular Face Box
for x, y, w, h in faces:
    img = cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 3)

# Resizing the image in order to display the image properly on the screen
resized = cv2.resize(img, (int(img.shape[1]), int(img.shape[0])))

# Displaying the image
cv2.imshow("Gray", resized)
cv2.waitKey(0)
 
cv2.destroyAllWindows()
