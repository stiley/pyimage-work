# import the necessary packages
import argparse
import imutils
import cv2


def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation=inter)

    # return the resized image
    return resized



#
# # construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True, help="Path to the image")
# args = vars(ap.parse_args())
#
# # load the image and show it
# image = cv2.imread(args["image"])
# cv2.imshow("Original", image)
# cv2.waitKey()
#
# # we need to keep in mind aspect ratio so the image does not look skewed
# # or distorted -- therefore, we calculate the ratio of the new image to
# # the old image. Let's make our new image have a width of 150 pixels
#
# # to get the ratio we simply divide the new size by the old size
# r = 150.0 / image.shape[1]
#
# # then we calc the dimension using the ratio from above to apply to the Y co-ordinates
# dim = (150, int(image.shape[0] * r))
#
# # perform the actual resizing of the image
# resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
# cv2.imshow("Resized (Width)", resized)
# cv2.waitKey()
#
# # what if we wanted to adjust the height of the image? We can apply
# # the same concept, again keeping in mind the aspect ratio, but instead
# # calculating the ratio based on height -- let's make the height of the
# # resized image 50 pixels
# r = 50.0 / image.shape[0]
# dim = (int(image.shape[1] * r), 50)
#
# # perform the resizing
# resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
# cv2.imshow("Resized (Height)", resized)
# cv2.waitKey(0)
#
#
#
# # using our resize function
# resized2 = resize(image,width=200)
# cv2.imshow("Resized2 (Width)", resized2)
# cv2.waitKey(0)


## Quix
image = cv2.imread("./images/florida_trip_small.png")
cv2.imshow("Original", image)


# resize
resized3 = resize(image, width=100,height=None, inter=cv2.INTER_NEAREST)
cv2.imshow("Resized", resized3)
cv2.waitKey()
X=74
Y=20
(b, g, r) = resized3[X,Y]
print("Pixel at ({X},{Y}) - Red: {r}, Green: {g}, Blue: {b}".format(X=X,Y=Y,r=r, g=g, b=b))


#resize to twice origninal shape
(h, w) = image.shape[:2]
resized4 = resize(image, width=w*2,height=None, inter=cv2.INTER_CUBIC)
cv2.imshow("Resized", resized4)
cv2.waitKey()
X=367
Y=170
(b, g, r) = resized4[X,Y]
print("Pixel at ({X},{Y}) - Red: {r}, Green: {g}, Blue: {b}".format(X=X,Y=Y,r=r, g=g, b=b))




cv2.destroyAllWindows()