"""使用resize方法边改图像大小 reiseze会改变像素的大小"""

import cv2
import matplotlib.pyplot as plt

image = cv2.imread('./image/logo.png', cv2.IMREAD_GRAYSCALE)

# 调整
image_50x50 = cv2.resize(image,(231,71))
image_50x50.save('logo.png')
plt.imshow(image_50x50,cmap="gray"),plt.axis('off')
plt.show()