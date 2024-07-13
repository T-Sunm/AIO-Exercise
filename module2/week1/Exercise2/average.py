import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

img = mpimg.imread('module2\week1\Exercise2\images\dog.jpg')
sum_rgb = np.sum(img, axis=2)
gray_img_02 = np.round(sum_rgb / 3, 1)
print(gray_img_02[0, 0])

fig, axes = plt.subplots(1, 2, figsize=(10, 8))

axes[0].imshow(img)
axes[0].set_title("Original Image")

axes[1].imshow(gray_img_02, cmap='gray')
axes[1].set_title("Grayscale Image")
plt.show()
