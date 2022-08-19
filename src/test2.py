from PIL import Image
from PIL import ImageChops

path1 = 'E:\\2.样本数据\\CSI_0812\\images\\08-0086_r.jpg'
path2 = 'E:\\2.样本数据\\CSI_0812\\images\\08-liepian-0045_r.jpg'
im1 = Image.open(path1)
im2 = Image.open(path2)



# print(im1.size)
# print(im2.size)

# diff = ImageChops.difference(im1, im2)
# if diff.getbbox() is None:
#     print('相同')
# else:
#     print('不同')

# image_paths = list(Path('/Users/pepsiyoung/Downloads/im_diff').glob('**/*.jpg'))
# for i in enumerate(image_paths)
#     print(i)

