import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("./image/flowers.png",cv2.IMREAD_GRAYSCALE)
print(image)
print(image.shape)
image_bgr = cv2.imread("./image/flowers.png",cv2.IMREAD_COLOR)
# 需要将bgr模式转化为rbg格式
image_rgb = cv2.cvtColor(image_bgr,cv2.COLOR_BGR2RGB)
print(image_bgr)
# 显示图像
plt.imshow(image,cmap='gray'),plt.axis('off')
plt.show()