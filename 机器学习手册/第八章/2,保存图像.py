import cv2


image = cv2.imread('./image/flowers.png',cv2.IMREAD_GRAYSCALE)
cv2.imwrite('./image/flowers_new.jpg',image)

