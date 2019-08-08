# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# # load the image and show it
# image = cv2.imread(args["image"])
# cv2.imshow("Original", image)
#
# # flip the image horizontally
# flipped = cv2.flip(image, 1)
# cv2.imshow("Flipped Horizontally", flipped)
#
# X=235
# Y=259
# (b, g, r) = flipped[X,Y]
# print("Pixel at ({X},{Y}) - Red: {r}, Green: {g}, Blue: {b}".format(X=X,Y=Y,r=r, g=g, b=b))
#
#
# # flip the image vertically
# flipped = cv2.flip(image, 0)
# cv2.imshow("Flipped Vertically", flipped)
#
# # flip the image along both axes
# flipped = cv2.flip(image, -1)
# cv2.imshow("Flipped Horizontally & Vertically", flipped)
# cv2.waitKey(0)


###### Quiz

q2Image = cv2.imread(args["image"])
# flip horzintally
flipped1 = cv2.flip(q2Image, 1)
cv2.imshow("Flipped Horizontally", flipped1)
cv2.waitKey()
#rotate 45
# where is cnetre
(h, w) = flipped1.shape[:2]
print("Shape height={} width={}".format(h, w))

(centreX, centreY) = (w//2, h//2)
print("Centre = ({0},{1})".format(centreX, centreY))

# rotate our image by 45 degrees
M = cv2.getRotationMatrix2D((centreX, centreY), 45, 1.0)
quizRotated = cv2.warpAffine(flipped1, M, (w, h))
cv2.imshow("Flipped Horizontally rotated 45 degrees", quizRotated)
cv2.waitKey()

#flip vert
flipped3 = cv2.flip(quizRotated, 0)
cv2.imshow("Flipped Horizontally rotated 45 degrees then flipped vertically", flipped3)
cv2.waitKey()


X=189
Y=441
(b, g, r) = flipped3[X,Y]
print("Pixel at ({X},{Y}) - Red: {r}, Green: {g}, Blue: {b}".format(X=X,Y=Y,r=r, g=g, b=b))


cv2.destroyAllWindows()