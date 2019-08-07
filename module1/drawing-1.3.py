import numpy as np
import cv2


canvas = np.zeros((300, 300, 3), dtype="uint8")

# lets draw
green = (0, 255, 0)
cv2.line(canvas,(0, 0), (300, 300), green, 8) # which image, start, end, line_thickness

red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 3)


# rectangle

# draw a green 50x50 pixel square, starting at 10x10 and ending at 60x60
cv2.rectangle(canvas, (10, 10), (60, 60), green)

# draw another rectangle, this time we'll make it red and 5 pixels thick
cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)

# let's draw one last rectangle: blue and filled in
blue = (255, 0, 0)
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)

# draw a green 50x50 pixel square, starting at 10x10 and ending at 60x60
cv2.rectangle(canvas, (10, 10), (60, 60), green)


cv2.imshow("Canvas", canvas)
cv2.waitKey()