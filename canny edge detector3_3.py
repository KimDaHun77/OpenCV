import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)
print(kernel)
#C:\Users\ASUS\Desktop
path = r'C:\Users\ASUS\Desktop\visionsys\realcat.jpg'
img = cv2.imread(path)
#cv2.imshow("realcat",img)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2. imshow("GrayScale", imgGray)

imgBlur = cv2.GaussianBlur(imgGray, (11,11), 2)
cv2. imshow("Img Blur_2", imgBlur)

imgCanny = cv2.Canny(imgBlur,250,250)
cv2.imshow("img cat 2", imgCanny)

imgBlur = cv2.GaussianBlur(imgGray, (11,11), 0.5)
cv2. imshow("Img Blur_0.5maybe sharp", imgBlur)

imgCanny = cv2.Canny(imgBlur,250,250)
cv2.imshow("img cat 0.5", imgCanny)

cv2.waitKey(0)