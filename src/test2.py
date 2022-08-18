import shutil
import time
from pathlib import Path
from PIL import Image
from PIL import UnidentifiedImageError
import uuid
from fileWatch.my_utils import encrypt_md5
from hashlib import md5


# im = Image.open("/Users/pepsiyoung/userfiles/source/9-201140-B.jpg")
# im = Image.open("E:\\111.jpg")
# print(im.verify())

# my_str = time.strftime("%Y-%m-%d", time.localtime())
# print(my_str)

# path = '/Users/pepsiyoung/Downloads/licence.txt'
# with open(path, 'r') as f:
#     print(f.readline())
#     f.writelines('www')
