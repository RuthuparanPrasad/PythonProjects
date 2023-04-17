
"""
@author: Ruthuparan Prasad
Data and Question from: StrataScratch

Prompt: Select an image in RGB format and use the OpenCV Python library to transform it so that it resembles a pencil sketch.

Tips

1. Convert the RGB image to grayscale - this will turn the image into a classic black-and-white photo;
2. Invert the grayscale image - this is sometimes referred to as a negative image and can be used to enhance details;
3. Mix the grayscale image with the inverted blurry image - this can be done by dividing the pixel values of the grayscale image by the pixel values of the inverted blurry image; the result should resemble a pencil sketch;
4. Experiment by applying other transformations offered by the OpenCV library to improve the effect;

"""

import cv2
import numpy as np

# reading the file
image = cv2.imread("dog.jpg")

# convert to grayscale
greyscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# adding gaussian blur 
blurred_image = cv2.GaussianBlur(greyscale_image, ksize = (11, 11), sigmaX = 3)

# inverting the image
inverted_image = cv2.bitwise_not(blurred_image)

# creating pencil sketch
pencil_sketch = cv2.divide(greyscale_image, inverted_image, scale = 255)

# save output before adding text
cv2.imwrite("pencil_sketch.jpg", pencil_sketch)


# defining the text variables
position = (550,70)
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 0.8
fontColour = (0,0,0)
thickness = 2
lineType = 2

# adding text to all images

cv2.putText(greyscale_image, "Greyscale Image",
                              position, font, fontScale, fontColour, 
                              thickness, lineType)

cv2.putText(blurred_image, "Blurred Image",
                              position, font, fontScale, fontColour, 
                              thickness, lineType)

cv2.putText(inverted_image, "Inverted Image",
                              position, font, fontScale, (255, 255, 255), 
                              thickness, lineType)
cv2.putText(pencil_sketch, "Pencil Sketch",
                              position, font, fontScale, fontColour, 
                              thickness, lineType)


# placing images in a grid
top_row = np.concatenate((greyscale_image, blurred_image), axis = 1)
bottom_row = np.concatenate((inverted_image, pencil_sketch), axis = 1)
final_image = np.concatenate((top_row, bottom_row), axis = 0)

# save image grid
cv2.imwrite("final_output.jpg", final_image)
