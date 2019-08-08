# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

# ### Erosion
# # apply a series of erosions
# for i in range(0, 3):
#     eroded = cv2.erode(gray.copy(), None, iterations=i + 1)
#     cv2.imshow("Eroded {} times".format(i + 1), eroded)
#     cv2.waitKey(0)
#
# ### Dialatioin
# for i in range(0, 3):
#     dialated = cv2.dilate(gray.copy(), None, iterations=i + 1)
#     cv2.imshow("Dialated {} times".format(i + 1), dialated)
#     cv2.waitKey(0)

# close all windows to cleanup the screen and initialize the list
# of kernels sizes that will be applied to the image
cv2.destroyAllWindows()
cv2.imshow("Original", image)
cv2.waitKey()


kernelSizes = [(3, 3), (5, 5), (7, 7)]

# loop over the kernels and apply an "opening" operation to the image
for kernelSize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    cv2.imshow("Opening: ({}, {})".format(kernelSize[0], kernelSize[1]), opening)
    cv2.waitKey(0)
cv2.destroyAllWindows()