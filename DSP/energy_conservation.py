# import cv2
# import numpy as np
# import matplotlib.pyplot as plt

# # plt.figure(figsize=(6.4*5, 4.8*5), constrained_layout=False)

# # img_c1 = cv2.imread("left01.jpg", 0)
# # img_c2 = np.fft.fft2(img_c1)
# # img_c3 = np.fft.fftshift(img_c2)
# # img_c4 = np.fft.ifftshift(img_c3)
# # img_c5 = np.fft.ifft2(img_c4)

# # plt.subplot(151), plt.imshow(img_c1, "gray"), plt.title("Original Image")
# # plt.subplot(152), plt.imshow(np.log(1+np.abs(img_c2)), "gray"), plt.title("Spectrum")
# # plt.subplot(153), plt.imshow(np.log(1+np.abs(img_c3)), "gray"), plt.title("Centered Spectrum")
# # plt.subplot(154), plt.imshow(np.log(1+np.abs(img_c4)), "gray"), plt.title("Decentralized")
# # plt.subplot(155), plt.imshow(np.abs(img_c5), "gray"), plt.title("Processed Image")

# # plt.show()

# # load and display image until any key is pressed
# image = cv2.imread("C:\\NOBLEAUSTINE\\GitWorld\\semester4\\DSP\\photo.jpg")
# # cv2.imshow('original', image)
# # cv2.waitKey(0)

# # displaying after converting the image to grey scale
# grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# # cv2.imshow('greyscale', grey_image)
# # cv2.waitKey(0)  

# # displaying after performing fft on the grey scale image
# # fft_image = np.fft.fft2(grey_image)
# fft_image = np.fft.fft2(image)
# cv2.imshow("fft",np.log(1+np.abs(fft_image)))
# # print(np.log(1+np.abs(fft_image)))
# cv2.waitKey(0)  


# import cv2 as cv
# import numpy as np
# from matplotlib import pyplot as plt

# img = cv.imread('C:\\NOBLEAUSTINE\\GitWorld\\semester4\\DSP\\photo.jpg', cv.IMREAD_GRAYSCALE)

# f = np.fft.fft2(img)
# i = np.fft.ifft2(f)
# print(img[0][0])
# print(i[0][0])

# fshift = np.fft.fftshift(f)
# magnitude_spectrum = 20*np.log(np.abs(fshift))


# plt.subplot(1,4,1),plt.imshow(img)
# plt.subplot(1,4,2),plt.imshow(img, cmap = 'gray')
# plt.title('Input Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(1,4,3),plt.imshow(magnitude_spectrum, cmap = 'gray')
# plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
# plt.subplot(1,4,4),plt.imshow(i, cmap = 'gray')
# plt.suptitle("PARSVELS ENERGY THEOREM")
# plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Create a Sine function
dt = 0.001 # Time steps
t = np.arange(0,10,dt) # Time array
f = np.sin(np.pi*t) # Sine function
# f = np.sin(np.pi*t)+1 # Sine function with DC offset
N = len(t) # Number of samples
plt.plot(t,f)
plt.show()

# Energy of function in time domain
energy_t = np.sum(abs(f)**2)

# Energy of function in frequency domain
# FFT = np.sqrt(2) * np.fft.rfft(f) 
FFT = np.sqrt(2) * np.fft.rfft(f) # only positive frequencies; correct magnitude due to discarding of negative frequencies

FFT[0] /= np.sqrt(2) # DC magnitude does not have to be corrected
FFT[-1] /= np.sqrt(2) # Nyquist frequency does not have to be corrected
frq = np.fft.rfftfreq(N,d=dt) # FFT frequenices


# Energy of function in frequency domain
energy_f = np.sum(abs(FFT)**2) / N

print('Parsevals theorem fulfilled: ' + str(round(energy_t - energy_f)))

# Parsevals theorem with proper sample points

energy_t = np.sum(abs(f)**2)
energy_f = np.sum(abs(FFT)**2) / N

print('Parsevals theorem NOT fulfilled: ' + str(round(energy_t - energy_f)))



back = np.fft.irfft(FFT) 
plt.plot(t,back)
plt.show()