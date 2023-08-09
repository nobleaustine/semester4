# importing required libraries
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# opening an image as a matrix img
img = cv.imread('C:\\NOBLEAUSTINE\\GitWorld\\semester4\\DSP\\abhishekMohan.jpeg', cv.IMREAD_GRAYSCALE)

# performing the 2d-DFT
# keeping the transformation as unitary by making norm = 'ortho'
img_FD   = np.fft.fft2(img, norm = 'ortho')


# calculating the energy of the signal as the l2 norm of the signal
mag_img    = np.linalg.norm(img,2,keepdims=False)
mag_img_FD = np.linalg.norm(img_FD,2,keepdims=False)


# taking the absolute value of complex terms to 
# display the image and adding log scale to display
# in the grey scale
img_FD_dis = np.log(np.absolute(img_FD))

# displaying the image taken for analysis 
plt.subplot(1,2,1),plt.imshow(img, cmap = 'gray')
plt.xlabel(f'Energy : {round(mag_img,3)}')
plt.title('intial image'), plt.xticks([]), plt.yticks([])


# displaying the DFT of image   
plt.subplot(1,2,2),plt.imshow(img_FD_dis, cmap = 'gray')
plt.xlabel(f'Energy : {round(mag_img_FD,3)}')
plt.title('DFT of image'), plt.xticks([]), plt.yticks([])

plt.suptitle("PARSVEL'S ENERGY THEOREM")
plt.show()




