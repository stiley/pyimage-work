# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image and convert it to grayscale
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# apply histogram equalization to stretch the contrast of our image
eq = cv2.equalizeHist(image)

# show our images -- notice how the contrast of the second image has
# been stretched
cv2.imshow("Original", image)
cv2.imshow("Histogram Equalization", eq)


# X=272
# Y=146
# Z = eq[X,Y]
#
# print("Z=".format(Z))
#
# print("Pixel at ({X},{Y}) - Red: {r}, Green: {g}, Blue: {b}".format(X=X,Y=Y,r=r, g=g, b=b))


cv2.waitKey(0)