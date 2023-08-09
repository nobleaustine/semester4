# import cv2
# import numpy as np
# import matplotlib.pyplot as plt

# # Load image in grayscale
# img = cv2.imread('/content/lena_gray.bmp', 0)

# # Compute the magnitude of the original image
# magnitude_original = np.abs(img) 

# # Calculate energy of input image
# energy_input = np.sqrt(np.sum(np.square(magnitude_original))/img.size)


# # Calculate DFT
# dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)

# # Shift DFT components to center
# dft_shift = np.fft.fftshift(dft)

# # Calculate magnitude spectrum
# magnitude_spectrum = 20 * np.log(1.2+cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

# # Scale the magnitude for inverse transform
# magnitude_spectrum = cv2.normalize(magnitude_spectrum, None, 0, 255, cv2.NORM_MINMAX,cv2.CV_8UC1)

# # Calculate energy of transformed image
# img_back = cv2.idft(dft, flags=cv2.DFT_COMPLEX_OUTPUT)
# img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])


# # Compute the magnitude of the original image
# magnitude_transformed = np.abs(magnitude_spectrum) 
# energy_transformed = np.sqrt(np.sum(np.square(magnitude_transformed))/magnitude_spectrum.size)

# print("energy input : ",energy_input)
# print("\nmagnitude_input :\n",magnitude_original)
# print("\nenergy output : ",energy_transformed)
# print("\nmagnitude_output :\n",magnitude_transformed)

# plt.subplot(121), plt.imshow(img, cmap="gray")
# plt.title("Input Image"), plt.xticks([]), plt.yticks([])

# plt.subplot(122), plt.imshow(magnitude_spectrum, cmap="gray")
# plt.title("Magnitude Spectrum"), plt.xticks([]), plt.yticks([])

# plt.show()

# plt.subplot(122), plt.imshow(img_back, cmap="gray")
# plt.title("Restored Image"), plt.xticks([]), plt.yticks([])
# plt.show()

import re
element = "3x1 + 4x2 + 3x3 "
result=re.findall(r'[x]\d+', element)
print(result)

