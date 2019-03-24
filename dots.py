import cv2
import numpy as np
import matplotlib.pyplot as plt

# RGB colors
mag = [(125,0,255),(255,0,255)]
red =[(200,0,0),(255,100,100)]
yell =[(175,255,0),(255,255,0)]

maps = ['fountains','memories','shrines']
colors = [mag,red,yell]

for i,m in enumerate(maps):

    # Load images
    img = cv2.imread('maps/'+str(m)+'.png')

    # Blur images
    blur_img = cv2.medianBlur(img,19)

    # Smoothie
    test = blur_img.copy()
    test = test.astype(np.float32)/255
    test = np.power(test,6)

    # Thresholding
    ret,th1 = cv2.threshold(test,0.45,1.0,cv2.THRESH_BINARY)

    # Uint8
    x = th1.copy()
    x = x.astype(np.uint8)*255

    # mask
    mask1 = cv2.inRange(x,colors[i][0],colors[i][1])

    # final mask and masked
    mask = cv2.bitwise_or(mask1,mask1)
    target = cv2.bitwise_and(x,x, mask=mask)

    # save images
    cv2.imwrite('outputs/'+str(m)+'_dots.png',target)
