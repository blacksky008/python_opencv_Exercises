import cv2
# 加载灰度图
img = cv2.imread('1.png', 0)
cv2.namedWindow('1', cv2.WINDOW_NORMAL)
cv2.imshow('1', img)
k = cv2.waitKey(0)
if k == ord('s'):
	cv2.imwrite('lena_gray.jpg', img)
