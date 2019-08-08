import numpy as np
import argparse
import imutils
import cv2

# #construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True, help="Path to the image")
# args = vars(ap.parse_args())
#
# # load the image and show it
# image = cv2.imread(args["image"])
# cv2.imshow("Original", image)
# cv2.waitKey()
#
# # where is cnetre
# (h, w) = image.shape[:2]
# print("Shape height={} width={}".format(h, w))
#
# (centreX, centreY) = (w//2, h//2)
# print("Centre = ({0},{1})".format(centreX, centreY))
#
# # rotate
#
# # rotate our image by 45 degrees
# M = cv2.getRotationMatrix2D((centreX, centreY), 45, 1.0)
# rotated = cv2.warpAffine(image, M, (w, h))
# cv2.imshow("Rotated by 45 Degrees", rotated)
# cv2.waitKey()
#
# # rotate our image by -90 degrees
# M = cv2.getRotationMatrix2D((centreX, centreY), -90, 1.0)
# rotated = cv2.warpAffine(image, M, (w, h))
# cv2.imshow("Rotated by -90 Degrees", rotated)
# cv2.waitKey()


# quiz questions
quizImage = cv2.imread("./images/wynn.png")
cv2.imshow("Quiz Image",quizImage)
cv2.waitKey()

#Q1 rotate by 30 degrewes clockwize

# where is cnetre
(h, w) = quizImage.shape[:2]
print("Shape height={} width={}".format(h, w))

(centreX, centreY) = (w//2, h//2)
print("Centre = ({0},{1})".format(centreX, centreY))

# rotate our image by 45 degrees
M = cv2.getRotationMatrix2D((50,50), 88, 1.0)
quizRotated = cv2.warpAffine(quizImage, M, (w, h))
cv2.imshow("Rotated by -30 Degrees", quizRotated)
cv2.waitKey()

# get pixel @ 335,254

X=10
Y=10
(b, g, r) = quizRotated[X,Y]
print("Pixel at ({X},{Y}) - Red: {r}, Green: {g}, Blue: {b}".format(X=X,Y=Y,r=r, g=g, b=b))

# (b, g, r) = quizRotated[312,136]
# print("Pixel at ({x},{y}) - Red: {r}, Green: {g}, Blue: {b}".format(x=312,y= 136,r=r, g=g, b=b))

cv2.destroyAllWindows()
