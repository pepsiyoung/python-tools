import numpy as np
from PIL import Image
from pathlib import Path

# im = Image.open(r'E:\temp\1.jpg').convert('RGB')
# im_data = np.array(im)
# print(im_data.shape)
# print(im.mode)
# im_data_new = np.concatenate((im_data[:1400, ::-1, :], im_data[1400:, :, :]), axis=0)
# print(im_data_new.shape)
# #
# im_target = Image.fromarray(im_data_new)
# im_target.show()

# n1 = np.array([[1, 2, 3], [4, 5, 6]])
# print(n1.shape)
# n2 = np.array([[7, 8, 9]])
# print(n2.shape)
# n3 = np.concatenate((n1, n2), axis=0)
# print(n3)


# def a():
#     param = 'b'  # 这里就会出现这样的提示，因为在main定义的param对象被重新指定了新的值
#     print(param)
#
#
# if __name__ == '__main__':
#     param = 'a'
#     a()


a = (1, 2, 3, 4)

for item in a:
    print(type(item))