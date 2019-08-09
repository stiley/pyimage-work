# import the necessary packages
################################################################
# See this page for discussion https://gurus.pyimagesearch.com/topic/finding-and-drawing-contours/
################################################################

import numpy as np
import argparse
import cv2
import imutils

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# show the original image
cv2.imshow("Original", image)

# find all contours in the image and draw ALL contours on the image
cnts = cv2.findContours(gray.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
clone = image.copy()
cv2.drawContours(clone, cnts, -1, (0, 255, 0), 2)
print("Found {} contours".format(len(cnts)))

# show the output image
cv2.imshow("All Contours", clone)



clone2 = image.copy()

# loop over the contours individually and draw each of them
for (i, c) in enumerate(cnts):
	print("Drawing contour #{}".format(i + 1))
	cv2.drawContours(clone2, [c], -1, (0, 255, 0), 2)
	cv2.imshow("Single Contour", clone2)
	cv2.waitKey()



#### Now above we find all contours, lets just do the external ones
clone3 = image.copy()
gray2 = cv2.cvtColor(clone3, cv2.COLOR_BGR2GRAY)
cv2.imshow("Looking for outside coutours", gray2)

# find all contours in the image and draw ALL contours on the image
contours = cv2.findContours(gray2.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # note the cv2.RETR_EXTERNAL
contours = imutils.grab_contours(contours)
print("here")
cv2.drawContours(clone3, contours, -1, (255, 0, 0), 3)
print("here")
# show the output image
cv2.imshow("All Contours new", clone3)
print("here")

cv2.waitKey()
cv2.destroyAllWindows()

clone = image.copy()
cv2.destroyAllWindows()

# loop over the contours individually
for c in contours:
    # construct a mask by drawing only the current contour
    mask = np.zeros(gray2.shape, dtype="uint8")
    cv2.drawContours(mask, [[c]], -1, 255, -1)

    # show the images
    cv2.imshow("Image", image)
    cv2.imshow("Mask", mask)
    cv2.imshow("Image + Mask", cv2.bitwise_and(image, image, mask=mask))
    cv2.waitKey()


cv2.waitKey()
cv2.destroyAllWindows()