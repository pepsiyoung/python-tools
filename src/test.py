from PIL import Image
from PIL import ImageChops
from pathlib import Path
from tqdm import tqdm
import shutil
import time

# path1 = '/Users/pepsiyoung/Downloads/虚焊漏检对比图片/未检测出/8-175734-A.jpg'
# path2 = '/Users/pepsiyoung/Downloads/虚焊漏检对比图片/未检测出/8-175938-B.jpg'
# im1 = Image.open(path1)
# im2 = Image.open(path2)

# diff = ImageChops.difference(im1, im2)
# if diff.getbbox() is None:
#     print('相同')
# else:
#     print('不同')

# image_paths = list(Path('/Users/pepsiyoung/Downloads/im_diff').glob('**/*.jpg'))
# for i in enumerate(image_paths)
#     print(i)

context_list = []
with open('E:\\pythonDemo\\9-1.jpg', 'rb') as f:
    # context_list.extend(str(item) for item in f.readlines())
    context_list.extend(f.readlines())

with open('E:\\pythonDemo\\source\\1.jpg', 'wb') as f:
    for index, context in enumerate(context_list):
        if index % 100 == 0:
            print(index)
            time.sleep(0.1)
        f.write(context)
    print('end')
