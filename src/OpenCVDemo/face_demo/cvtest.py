import cv2 as cv
import numpy as np
from PIL import Image

# pic = cv.imread("../../img/catdog.jpg")
# cv.rectangle(pic, (70, 90), (170, 190), color=(0, 0, 255), thickness=2)
# cv.imshow('title', pic)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# # print(pic)


# k = cv.waitKey(1) & 0xff
# print("key:")
# print(k)
im = Image.open('/Users/pepsiyoung/Project/my/python/python-tools/src/OpenCVDemo/face_demo/imgdata/1_Boss_1.jpg')
img = np.array(im)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
print(gray)
