# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image, grab its dimensions, and show it
image = cv2.imread(args["image"])
(h, w) = image.shape[:2]
print("Image height={}, image width={}".format(h,w))

# original color
(b,g,r) = image[0,0]
print("Pixel at (0, 0) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))

#lets manipulate the color
image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))
cv2.imshow("Original", image)
cv2.waitKey()

# lets show half the image

#Find the centre of the image
(cX,cY) = (w//2, h//2)

# since we are using NumPy arrays, we can apply slicing and grab large chunks

# of the image -- let's grab the top-left corner
tl = image[0:cY, 0:cX]
cv2.imshow("Top-Left Corner", tl)
cv2.waitKey()

#top right
tr = image[0:cY, cX:w]
cv2.imshow("Top-Right Corner", tr)
cv2.waitKey()

#bottom left
bl=image[cY:h, 0:cX]
cv2.imshow("Bottom-Left Corner", bl)
cv2.waitKey()

#bottom right
br=image[cY:h, cX:w]
cv2.imshow("Bottom-Right Corner", br)
cv2.waitKey()

# lets color the top left (B,G,R) BLUE
image[0:cY,0:cX] = (255,0,0)
cv2.imshow("top-left coloured", image)
cv2.waitKey()



# quiz

imageQuiz = cv2.imread('./images/florida_trip.png')
(b, g, r) = imageQuiz[225,111]
print("Pixel at (0, 0) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))




