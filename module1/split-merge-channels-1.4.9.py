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
18
19
20
21
22
23
24
25
26
27
28
# import the necessary packages
import numpy as np
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# Load the image and grab each channel: Red, Green, and Blue. It's
# important to note that OpenCV stores an image as NumPy array with
# its channels in reverse order! When we call cv2.split, we are
# actually getting the channels as Blue, Green, Red!
image = cv2.imread(args["image"])
(B, G, R) = cv2.split(image)

# show each channel individually
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey()

# merge the image back together again
merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)
cv2.waitKey()



# visualize each channel in color
zeros = np.zeros(image.shape[:2], dtype = "uint8")
redMerged = cv2.merge([zeros, zeros, R])
cv2.imshow("Red", redMerged)

greenMerged = cv2.merge([zeros, G, zeros])
cv2.imshow("Green",greenMerged)

blueMerged = cv2.merge([B, zeros, zeros])
cv2.imshow("Blue", blueMerged)
cv2.waitKey(0)


X=5
Y=80
(b, g, r) = greenMerged[X,Y]
print("Pixel at ({X},{Y}) - Red: {r}, Green: {g}, Blue: {b}".format(X=X,Y=Y,r=r, g=g, b=b))

cv2.destroyAllWindows()