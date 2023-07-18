import cv2
import numpy as np



def resize(image):
    return cv2.resize(image, (1848, 4272))

def gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def flip(image):
    return cv2.flip(image, 1)


def addBorder(image):
    return cv2.copyMakeBorder(image, 10, 10, 10, 10, cv2.BORDER_CONSTANT, None, value = 0)


def blur(image):
    return cv2.blur(image, (15, 15))












# # Loading the image
# image = cv2.imread('images/desktop.jpeg', 1)
# cv2.imshow('Original', image)
# cv2.waitKey(0)

# # 1- gray  
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Grayscale', gray_image)
# cv2.waitKey(0)  


# # 2- resize
# resize_image = cv2.resize(image, (1848, 4272))
# cv2.imshow('Resize', resize_image)
# cv2.waitKey(0) 

# # 3- Blur
# blur_image = cv2.blur(image, (15, 15))
# cv2.imshow('Blurring', blur_image)
# cv2.waitKey(0)

# # 4- flip
# flip_image = cv2.flip(image, 1)
# cv2.imshow('Flipping', flip_image)
# cv2.waitKey(0)


# # 5- add border
# bordered_image = cv2.copyMakeBorder(image, 10, 10, 10, 10, cv2.BORDER_CONSTANT, None, value = 0)
# cv2.imshow('Border', bordered_image)
# cv2.waitKey(0)


# # Window shown waits for any key pressing event
# cv2.destroyAllWindows()