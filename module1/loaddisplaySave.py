import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True ,help="Path to the source image")

args = vars(ap.parse_args())
print(args)

image = cv2.imread(args["image"])
print("width: %d pixels" % (image.shape[1]))
print("height: %d pixels" % (image.shape[0]))
print("channels: %d" % (image.shape[2]))

cv2.imshow("Image", image)
cv2.waitKey()

cv2.imwrite("new_image.jpg", image)