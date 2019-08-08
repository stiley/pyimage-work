2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
# import the necessary packages
import cv2

# load the image and show it
image = cv2.imread("./images/florida_trip.png")
cv2.imshow("Original", image)

# cropping an image is accomplished using simple NumPy array slices --
# let's crop the face from the image
face = image[85:250, 85:220]
cv2.imshow("Face", face)
cv2.waitKey()

# ...and now let's crop the entire body
body = image[90:450, 0:290]
cv2.imshow("Body", body)
cv2.waitKey()
red = (0, 0, 255)

# cv2.line(image, (85, 85), (220, 220), red, 5)

cv2.imshow("Canvas", image)
cv2.waitKey()


try1 = image[173:235, 13:81]
cv2.imshow("try1", try1)
cv2.waitKey()


try2 = image[124:212, 225:380]
cv2.imshow("try2", try2)
cv2.waitKey()

try3 = image[90:450, 0:290]
cv2.imshow("try3", try3)
cv2.waitKey()


try4 = image[85:250, 85:220]
cv2.imshow("try4", try4)
cv2.waitKey()



cv2.destroyAllWindows()