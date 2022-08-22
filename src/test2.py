import torch
from torchvision import transforms
from PIL import Image
from PIL import ImageChops

# path1 = 'E:\\2.样本数据\\CSI_0812\\images\\08-0086_r.jpg'
# path2 = 'E:\\2.样本数据\\CSI_0812\\images\\08-liepian-0045_r.jpg'
path1 = '/Users/pepsiyoung/Downloads/ccc.jpg'
path2 = '/Users/pepsiyoung/Downloads/bbb.jpg'
im1 = Image.open(path1)
im2 = Image.open(path2)

# im1 = im1.convert("RGB")
# im1.save('/Users/pepsiyoung/Downloads/ccc.jpg')

print(im1.mode)
print(im2.mode)

# t1 = transforms.ToTensor()(im1)
# t2 = transforms.ToTensor()(im2)
# print(t1.shape)
# print(t2.shape)


# diff = ImageChops.difference(im1, im2)
# if diff.getbbox() is None:
#     print('相同')
# else:
#     print('不同')

# image_paths = list(Path('/Users/pepsiyoung/Downloads/im_diff').glob('**/*.jpg'))
# for i in enumerate(image_paths)
#     print(i)

