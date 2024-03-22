import numpy as np
import cv2
from matplotlib import pyplot as plt

img1=cv2.imread(r'C:\Users\ASUS\Desktop\visionsys\realcat.jpg',0)
img2=cv2.imread(r'C:\Users\ASUS\Desktop\visionsys\realcat.jpg',0)
cv2.imshow("Query image", img1)
cv2.imshow("Reference image", img2)

sift = cv2.SIFT_create()

kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)

bf=cv2.BFMatcher()
matches=bf.knnMatch(des1,des2,k=2)

good = []
for m,n in matches:
    if m.distance < 0.1*n.distance:
        good.append([m])

img3=cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)

#img4=cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,img3,flags=1)

cv2.imshow("matching",img3),plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()