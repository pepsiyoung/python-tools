import shutil
import time
from pathlib import Path
from tqdm import tqdm
from PIL import Image
from PIL import UnidentifiedImageError


# paths = Path(r'E:\pythonDemo\image').glob('**/*.jpg')
# for path in tqdm(list(paths)):
#     shutil.copy(path, Path(r'E:\pythonDemo\source\222'))

# fo = open("E:\\pythonDemo\\image\\222\\08-0001.jpg", "w")
# print("文件名: ", fo.name)

# im = Image.open("/Users/pepsiyoung/userfiles/source/9-201140-B.jpg")
# im = Image.open("E:\\111.jpg")
# print(im.verify())

my_str = time.strftime("%Y-%m-%d", time.localtime())
print(my_str)


# k = Path('E:\\detectImage\\8-14-8\\8-150638-A.jpg').parent
# print(k)


# sleep_count = 0
#
# while not valid_image('E:\\1114.jpg') and sleep_count < 4:
#     time.sleep(0.5)
#     sleep_count += 1
#     print(sleep_count)
#
# print('end')
