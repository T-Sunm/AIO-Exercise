import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('module2\week1\Exercise2\images\dog.jpg')
sum_rgb = np.sum(img, axis=2)
gray_img_02 = np.round(sum_rgb / 3, 1)
print(gray_img_02[0, 0])
