from PIL import Image
from PIL import ImageChops
from pathlib import Path
from tqdm import tqdm
import shutil

path1 = '/Users/pepsiyoung/Downloads/虚焊漏检对比图片/未检测出/8-175734-A.jpg'
path2 = '/Users/pepsiyoung/Downloads/虚焊漏检对比图片/未检测出/8-175938-B.jpg'
im1 = Image.open(path1)
im2 = Image.open(path2)

#
# diff = ImageChops.difference(im1, im2)
# if diff.getbbox() is None:
#     print('相同')
# else:
#     print('不同')

# image_paths = list(Path('/Users/pepsiyoung/Downloads/im_diff').glob('**/*.jpg'))
# for i in enumerate(image_paths)
#     print(i)

print(Path(im1))