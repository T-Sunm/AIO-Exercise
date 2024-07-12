import gdown
import os
import matplotlib.image as mpimg
import numpy as np
# # URL tệp trên Google Drive
# url = 'https://drive.google.com/uc?id=1i9dqan21DjQoG5Q_VEvm0LrVwAlXD0vB'

# # Thư mục đích
# output_folder = 'images'
# # Tên tệp đích
# output_file = 'dog.jpg'
# # Tạo thư mục nếu chưa tồn tại
# if not os.path.exists(output_folder):
#   os.makedirs(output_folder)

# # Đường dẫn đầy đủ tới tệp đích
# output_path = os.path.join(output_folder, output_file)
# # Tải tệp
# gdown.download(url, output_path, quiet=False)

img = mpimg.imread('module2\week1\Exercise2\images\dog.jpg')
max_rgb = np.max(img, axis=2)
min_rgb = np.min(img, axis=2)
gray_img_01 = np.round((max_rgb + min_rgb) / 2, 1)
print(gray_img_01[0, 0])


