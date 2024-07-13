import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt

# Cách 1
img = mpimg.imread('module2\week1\Exercise2\images\dog.jpg')
coef = np.array([0.21, 0.72, 0.07])
gray_img_03 = np.zeros((img.shape[0], img.shape[1]))
print(img.shape[0])
for i in range(img.shape[0]):
  for j in range(img.shape[1]):
    gray_img_03[i, j] = np.round(img[i, j].dot(coef), 1)

print(gray_img_03[0, 0])


# cách 2
def compute_luminosity(vector):
  coef = np.array([0.21, 0.72, 0.07]).T
  return np.round(vector.dot(coef), 1)


gray_img_03 = np.apply_along_axis(compute_luminosity, axis=2, arr=img)
print(gray_img_03[0, 0])

fig, axes = plt.subplots(1, 2, figsize=(10, 8))

axes[0].imshow(img)
axes[0].set_title("Original Image")

axes[1].imshow(gray_img_03, cmap='gray')
axes[1].set_title("Grayscale Image")

plt.show()
