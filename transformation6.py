import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r'C:\Users\ASUS\Desktop\visionsys\TabletPC.jpg',0)#make rectangle
cv2.imshow('Input',img)

rows,cols = img.shape

pts1 = np.float32([[76,489],[225,1247],[903,434],[984,931]])#Take the coordinates of the corners
pts2 = np.float32([[0,0],[0,200],[200,0],[200,200]])

M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(200,200))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()