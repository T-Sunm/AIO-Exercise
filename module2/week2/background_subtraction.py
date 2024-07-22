import matplotlib.pyplot as plt
import cv2
import numpy as np

def compute_difference(bg_img, input_img):
  difference_single_channel = bg_img - input_img
  return difference_single_channel

def compute_binary_mask(difference_single_channel):
  _, difference_binary = cv2.threshold(
      difference_single_channel, 50, 255, cv2.THRESH_BINARY)
  return difference_binary

def replace_background(bg_img, obj_img, binary_mask):
  final_output = np.where(binary_mask == 0, bg_img, obj_img)
  return final_output

def main():
  green_background = cv2.imread(
      "image_data/GreenBackground.png")
  green_background = cv2.cvtColor(green_background, cv2.COLOR_BGR2RGB)
  green_background = cv2.resize(green_background, (678, 381))

  new_background = cv2.imread(
      "image_data/NewBackground.jpg")
  new_background = cv2.cvtColor(new_background, cv2.COLOR_BGR2RGB)
  new_background = cv2.resize(new_background, (678, 381))

  obj = cv2.imread(
      "image_data/Object.png")
  obj = cv2.cvtColor(obj, cv2.COLOR_BGR2RGB)
  obj = cv2.resize(obj, (678, 381))

  difference_single_channel = compute_difference(green_background, obj)
  binary_mask = compute_binary_mask(difference_single_channel)
  final_output = replace_background(new_background, obj, binary_mask)
  _, axs = plt.subplots(2, 2)
  axs[0, 0].imshow(green_background)
  axs[0, 0].set_title("Original Background Image")

  axs[0, 1].imshow(new_background)
  axs[0, 1].set_title("Target Background Image")

  axs[1, 0].imshow(obj)
  axs[1, 0].set_title("Object Image")

  axs[1, 1].imshow(final_output)
  axs[1, 1].set_title("Final output")

  plt.show()


if __name__ == "__main__":
  main()
