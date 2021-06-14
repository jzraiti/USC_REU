import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#find lake image file
img = cv.imread(cv.samples.findFile("lake_png.png"))

cv.imshow("Display window", img)
k = cv.waitKey(10*1000)
#convert to bianary
ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)

#plot
cv.imshow("Display window", thresh1)
k = cv.waitKey(10*1000)

cv.imwrite("lake_blackandwhite.png", thresh1)