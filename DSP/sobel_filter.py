import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def convolve2D(image, kernel, padding=0, strides=1):
    # Cross Correlation
    kernel = np.flipud(np.fliplr(kernel))

    # Gather Shapes of Kernel + Image + Padding
    xKernShape = kernel.shape[0]
    yKernShape = kernel.shape[1]
    xImgShape = image.shape[0]
    yImgShape = image.shape[1]

    # Shape of Output Convolution
    xOutput = int(((xImgShape - xKernShape + 2 * padding) / strides) + 1)
    yOutput = int(((yImgShape - yKernShape + 2 * padding) / strides) + 1)
    output = np.zeros((xOutput, yOutput))

    # Apply Equal Padding to All Sides
    if padding != 0:
        imagePadded = np.zeros((image.shape[0] + padding*2, image.shape[1] + padding*2))
        imagePadded[int(padding):int(-1 * padding), int(padding):int(-1 * padding)] = image
        print(imagePadded)
    else:
        imagePadded = image

    # Iterate through image
    for y in range(image.shape[1]):
        # Exit Convolution
        if y > image.shape[1] - yKernShape:
            break
        # Only Convolve if y has gone down by the specified Strides
        if y % strides == 0:
            for x in range(image.shape[0]):
                # Go to next row once kernel is out of bounds
                if x > image.shape[0] - xKernShape:
                    break
                try:
                    # Only Convolve if x has moved by the specified Strides
                    if x % strides == 0:
                        output[x, y] = (kernel * imagePadded[x: x + xKernShape, y: y + yKernShape]).sum()
                except:
                    break

    return output

img = cv.imread('C:\\NOBLEAUSTINE\\GitWorld\\semester4\\DSP\\photo.jpg',cv.IMREAD_COLOR)
i = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("image", img)
# cv.waitKey(0)
# cv.imshow("image", gray_image)
# cv.waitKey(0)
filter1 = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
filter2 = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
filter3 = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
filter4 = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])

matrix = np.array(i)
pad_height = filter1.shape[0] - 1
pad_width = filter1.shape[1] - 1
padded_image = np.pad(matrix, ((pad_height, pad_height), (pad_width, pad_width)), mode='constant')


output_image1 = convolve2D(padded_image, filter1, padding=0, strides=1)
output_image2 = convolve2D(padded_image, filter2, padding=0, strides=1)
output_image3 = convolve2D(padded_image, filter3, padding=0, strides=1)
output_image4 = convolve2D(padded_image, filter4, padding=0, strides=1)
output = (output_image1**2 + output_image2**2)**0.5
plt.subplot(1,6,1),plt.imshow(padded_image,cmap='gist_gray')
plt.xticks([]), plt.yticks([])
plt.subplot(1,6,2),plt.imshow(output,cmap='gist_gray')
plt.xticks([]), plt.yticks([])
plt.subplot(1,6,3),plt.imshow(output_image3,cmap='gist_gray')
plt.xticks([]), plt.yticks([])
plt.subplot(1,6,4),plt.imshow(output_image4,cmap='gist_gray')
plt.xticks([]), plt.yticks([])
plt.subplot(1,6,5),plt.imshow(output_image1,cmap='gist_gray')
plt.xticks([]), plt.yticks([])
plt.subplot(1,6,6),plt.imshow(output_image2,cmap='gist_gray')
plt.xticks([]), plt.yticks([])
plt.show()


# plt.subplot(1,3,1),plt.imshow(img)
# plt.xticks([]), plt.yticks([])
# plt.subplot(1,3,2),plt.imshow(gray_image)
# plt.xticks([]), plt.yticks([])
# plt.subplot(1,3,3),plt.imshow(img, cmap = 'gray')
# plt.xticks([]), plt.yticks([])
# # plt.title('Input Image'), 
# # plt.subplot(1,4,3),plt.imshow(magnitude_spectrum, cmap = 'gray')
# # plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
# # plt.subplot(1,4,4),plt.imshow(i, cmap = 'gray')
# # plt.suptitle("PARSVELS ENERGY THEOREM")
# plt.show()


import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# importing an image as img
img = cv.imread('C:\\NOBLEAUSTINE\\GitWorld\\semester4\\DSP\\new.jpg', cv.IMREAD_GRAYSCALE)

img_f      = np.fft.fft2(img,norm='ortho')
norm_img_f = np.divide(img_f,1)
i_img_f    = np.fft.ifft2(img_f,norm='ortho')

k1 = np.linalg.norm(img,2,keepdims=False)
mag_img = np.abs(img)
m1      = np.sum(mag_img)

k2= np.linalg.norm(norm_img_f,2,keepdims=False)
mag_norm_img_f = np.abs(norm_img_f)
m2             = np.sum(mag_norm_img_f)

k3 = np.linalg.norm(i_img_f,2,keepdims=False)
mag_i_img_f = np.abs(i_img_f)
m3          = np.sum(mag_i_img_f )

print(m1,m2,m3)
print(k1,k2,k3)

magnitude = np.log(mag_norm_img_f)


# fshift = np.fft.fftshift(f)
# magnitude_spectrum = 20*np.log(np.abs(fshift))

plt.subplot(1,3,1),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])

plt.subplot(1,3,2),plt.imshow(magnitude, cmap = 'gray')
plt.title('fft of image'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,3),plt.imshow(mag_i_img_f, cmap = 'gray')
plt.title('inverse of fft'), plt.xticks([]), plt.yticks([])
plt.suptitle("PARSVELS ENERGY THEOREM")
plt.show()