import cv2

# 加载灰度图
img = cv2.imread('1.jpg', 0)
#cv2.imshow('1', img)
#cv2.waitKey(0)
cv2.imwrite('lena_gray.jpg', img)