# import the necessary packages
import argparse
import cv2

import imutils
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image, convert it to grayscale, and blur it slightly
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)  # source, kernel size,
blurred2 = cv2.GaussianBlur(image, (3, 3), 0)  # source, kernel size,

# show the original and blurred images
cv2.imshow("Original", image)
cv2.imshow("Blurred", blurred)
cv2.imshow("Gray", gray)

# compute a "wide", "mid-range", and "tight" threshold for the edges
wide = cv2.Canny(blurred2, 10, 200)
mid = cv2.Canny(blurred2, 30, 150)
tight = cv2.Canny(blurred2, 240, 250)

auto = imutils.auto_canny(blurred2)


# show the edge maps
cv2.imshow("Wide Edge Map", wide)
cv2.imshow("Mid Edge Map", mid)
cv2.imshow("Tight Edge Map", tight)
cv2.imshow("Auto Edge Map", auto)
cv2.waitKey()



cv2.destroyAllWindows()