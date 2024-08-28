"""使用数组切片方便的裁剪图像"""

import cv2
import matplotlib.pyplot as plt

image = cv2.imread('./image/flowers.png', cv2.IMREAD_GRAYSCALE)

image_cropped = image[:,:40]

plt.imshow(image_cropped,cmap='gray'),plt.axis('off')
plt.show()