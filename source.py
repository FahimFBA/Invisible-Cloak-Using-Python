# start importing some modules

# importing OpenCV
import cv2
# using this module , we can process images and videos to identify objects, faces, or even handwriting of a human.

# importing NumPy
import numpy as np
# NumPy is usually imported under the np alias. NumPy is a Python library used for working with arrays. It also has functions for working in domain of linear algebra, fourier transform, and matrices

# importing another essential module named time
import time
# The Python time module provides many ways of representing time in code, such as objects, numbers, and strings. It also provides functionality other than representing time, like waiting during code execution and measuring the efficiency of our code.


 # I'll use a print function here. It's optional.

print("Hey! Have you ever heard about invisible cloak?")
print("What is an invisible cloak?")
print("""
 You have watched invisible cloak in "Harry Potter" a lot, haven't you?

            It's the same thing. How would I provide you that cloak?

            Grab a red cloth first! I'll convert that cloth into an invisible cloak with my project!!!


""")

# starting the initial part

cap = cv2.VideoCapture(0) # It lets you create a video capture object which is helpful to capture videos through webcam and then you may perform desired operations on that video.

# I need to suspend execution time for 1 seconds now. I'll used it to capture the still background image.
time.sleep(1)
background = 0 # background plot 

# capturing the live frame 
for i in range(30):
    ret,background = cap.read()

# flipping the image
background = np.flip(background,axis=1) 
while(cap.isOpened()):  
    ret, img = cap.read()  # reading from the ongoing video
    img = np.flip(img,axis=1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # Converting the image : from BGR to HSV
    value = (35, 35)
    blurred = cv2.GaussianBlur(hsv, value,0)

    # configuration for the mask1 

    lower_red = np.array([0,120,70])
    upper_red = np.array([10,255,255])
    mask1 = cv2.inRange(hsv,lower_red,upper_red)

    # configuration for the mask2 

    lower_red = np.array([170,120,70])
    upper_red = np.array([180,255,255])
    mask2 = cv2.inRange(hsv,lower_red,upper_red)

    # The upper blocks of code (mask1 and mask2) can be replaced with some other code depending the color of your cloth which you would use as the invisible cloak

    mask = mask1+mask2
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5,5),np.uint8)) # Morphological Transformations

    img[np.where(mask==255)] = background[np.where(mask==255)]
    cv2.imshow('Display',img) # display the image in the specified window
    k = cv2.waitKey(10) # cv2. waitKey() is a keyboard binding function. The function waits for specified milliseconds for any keyboard event.
    if k == 27:
        break

