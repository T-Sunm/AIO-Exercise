import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('module2\week1\Exercise2\images\dog.jpg')
coef = np.array([0.21, 0.72, 0.07])
gray_img_03 = np.zeros((img.shape[0], img.shape[1]))
print(img.shape[0])
for i in range(img.shape[0]):
  for j in range(img.shape[1]):
    gray_img_03[i, j] = np.round(img[i, j].dot(coef), 1)

print(gray_img_03[0, 0])
