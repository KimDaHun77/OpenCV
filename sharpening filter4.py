import cv2
import numpy as np
import matplotlib.pyplot as plt

filename = r'C:\Users\ASUS\Desktop\visionsys\realcat.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('before sharpening filter', gray)
blur= cv2.GaussianBlur(gray,(11,11),1.3)
alpha=2
gray=gray+alpha*(gray-blur)#샤프닝 추가

cv2.imshow('sharpening filter', gray)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)
plt.figure()
plt.imshow(dst)
plt.colorbar()
dst = cv2.dilate(dst,None)

plt.figure()
plt.imshow(dst)
plt.colorbar()

img[dst>0.01*dst.max()]=[0,0,255]

cv2.imshow('dst', img)
cv2.waitKey(0)
cv2.destroyAllWindows()