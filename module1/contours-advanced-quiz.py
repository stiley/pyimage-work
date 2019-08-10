# import the necessary packages
################################################################
# See this page for discussion https://gurus.pyimagesearch.com/quizzes/advanced-contour-properties-quiz/
################################################################


# import the necessary packages
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

# find external contours in the image
cnts = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
clone = image.copy()


# loop over the contours
for (i, c) in enumerate(cnts):
    # compute the area of the contour along with the bounding box
    # to compute the aspect ratio
    area = cv2.contourArea(c)
    (x, y, w, h) = cv2.boundingRect(c)
    print("Contour{0} - Bounding rectangle (x,y,w,h) = ({1},{2},{3},{4})".format(i+1, x, y, w, h))
    # compute the aspect ratio of the contour, which is simply the width
    # divided by the height of the bounding box
    aspectRatio = w / float(h)

    # use the area of the contour and the bounding box area to compute
    # the extent
    extent = area / float(w * h)

    # compute the convex hull of the contour, then use the area of the
    # original contour and the area of the convex hull to compute the
    # solidity
    hull = cv2.convexHull(c)
    hullArea = cv2.contourArea(hull)
    solidity = area / float(hullArea)
    print("Contour{} - aspect Ratio = {:.2f} - solidity={:.2f} - extent = {:.2f})".format(i + 1, aspectRatio, solidity, extent))
    cv2.drawContours(image, [c], -1, (0, 255, 0), 3)
    cv2.imshow("Contours", image)
    cv2.waitKey()

cv2.waitKey()
cv2.destroyAllWindows()