# import the necessary packages
################################################################
# See this page for discussion https://gurus.pyimagesearch.com/topic/advanced-contour-properties/
################################################################

# import the necessary packages
import cv2
import imutils

# load the tic-tac-toe image and convert it to grayscale
image = cv2.imread("images/tictactoe.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# find all contours on the tic-tac-toe board
cnts = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# loop over the contours
for (i, c) in enumerate(cnts):
    # compute the area of the contour along with the bounding box
    # to compute the aspect ratio
    area = cv2.contourArea(c)
    print("Area of contour = {0})".format(area))
    (x, y, w, h) = cv2.boundingRect(c)
    print("Bounding rectangle (x,y,w,h) = ({0},{1},{2},{3})".format(x, y, w, h))
    # compute the convex hull of the contour, then use the area of the
    # original contour and the area of the convex hull to compute the
    # solidity
    hull = cv2.convexHull(c)
    # print("Contour #{} Hull contour = {}".format( i + 1,hull))
    hullArea = cv2.contourArea(hull)
    # print("Contour #{} - Hull area = {}".format( i + 1,hullArea))
    solidity = area / float(hullArea)

    # show the contour properties
    print("Contour #{} -- solidity={:.2f}".format( i + 1, solidity))
    # initialize the character text
    char = "?"

    # if the solidity is high, then we are examining an `O`
    if solidity > 0.9:
        char = "O"

    # otherwise, if the solidity it still reasonabably high, we
    # are examining an `X`
    elif solidity > 0.5:
        char = "X"

    # if the character is not unknown, draw it
    if char != "?":
        cv2.drawContours(image, [c], -1, (0, 255, 0), 3)
        cv2.putText(image, ("Contour {}={}".format(i+1, char)), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.50,
                    (0, 255, 0), 1)



# show the output image
cv2.imshow("Output", image)
cv2.waitKey(0)
