import cv2
import numpy as np

image = cv2.imread(r'C:\Users\ASUS\Desktop\visionsys\realcat.jpg')
Gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("original image", Gray)
gx = cv2.Sobel(Gray, -1, 1, 0, ksize=3)
gx = cv2.Sobel(Gray, cv2.CV_32F, 1, 0, ksize=3)
gx = np.abs(gx)
gx = cv2.normalize(gx, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_32F)

gy = cv2.Sobel(Gray, -1, 0, 1, ksize=3)
gy = cv2.Sobel(Gray, cv2.CV_32F, 0, 1, ksize=3)
gy = np.abs(gy)
gy = cv2.normalize(gy, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_32F)

mag = cv2.magnitude(gx, gy)
mag = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
cv2.imshow("filtered image", mag)

cv2.waitKey(0)
cv2.destroyAllWindows()



