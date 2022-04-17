import numpy
import cv2

import matplotlib.pyplot as plt

sample_image_file = '/Users/leonyao/Documents/collagen_analysis/dataset/206-16 1 NSMF-C-day 7/206-16 1 NSMF-C-day 7_001.TIF'
img = cv2.imread(sample_image_file)
print(img)
plt.imshow(img)
plt.show()