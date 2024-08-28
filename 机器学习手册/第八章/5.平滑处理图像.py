import cv2
import matplotlib.pyplot as plt
import numpy as np
image = cv2.imread('./image/flowers.png', cv2.IMREAD_GRAYSCALE)
# 平滑处理
image_blurry = cv2.blur(image,(20,20))

plt.imshow(image_blurry,cmap='gray'),plt.axis('off')
plt.show()

# 使用自定义核来处理图像
kernel = np.ones((5,5))/25.0

image_kernel = cv2.filter2D(image,-1,kernel)
plt.imshow(image_kernel,cmap='gray'),plt.axis('off')
plt.show()
print(kernel)