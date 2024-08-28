import cv2
import matplotlib.pyplot as plt
import numpy as np
image = cv2.imread('./image/flowers.png', cv2.IMREAD_GRAYSCALE)

kernel = np.array([[0,-1,0],
                   [-1,6,-1],
                   [0,-1,0]])

image_kernel = cv2.filter2D(image,-1,kernel)
plt.imshow(image_kernel,cmap='gray'),plt.axis('off')
plt.show()