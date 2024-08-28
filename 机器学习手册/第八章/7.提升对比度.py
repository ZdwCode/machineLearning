"""直方图均衡是一种图像处理方法，它可以使图像中的物体和形状更加突出
    对于灰度图像可以直接用opencv的equalizeHist方法
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
image = cv2.imread('./image/flowers.png', cv2.IMREAD_GRAYSCALE)

image_enhanced = cv2.equalizeHist(image)

plt.imshow(image_enhanced,cmap='gray')
plt.show()

# 对于彩色图像 需要先将其转化为YUV格式，然后使用equalizehist方法

image_bgr = cv2.imread('./image/flowers.png',cv2.IMREAD_COLOR)
image_rgb = cv2.cvtColor(image_bgr,cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb),plt.axis('off')
plt.show()
print(image_rgb)
# 转化为YUV格式
image_yuv = cv2.cvtColor(image_rgb,cv2.COLOR_RGB2YUV)
print(image_yuv)
print(image_yuv[:,:,0])
# 对亮度那一层进行均衡化
image_yuv[:,:,0] = cv2.equalizeHist(image_yuv[:,:,0])

# 转化回RGB格式
image_rgb = cv2.cvtColor(image_yuv,cv2.COLOR_YUV2RGB)

plt.imshow(image_rgb),plt.axis('off')
plt.show()