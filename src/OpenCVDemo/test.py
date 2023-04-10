import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# img = cv.imread(r"C:\Users\admin\Desktop\zidane.jpg")
# # cv.imshow("test", img)
# # cv.waitKey(0)
#
# plt.imshow(img[:, :, ::-1])
# plt.show()


x = np.uint8([250])
y = np.uint8([10])

print(cv.add(x, y))
print(x + y)
